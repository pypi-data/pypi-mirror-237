from dask.distributed import LocalCluster, Client
from dask_gateway import Gateway
import os
import s3fs
import sys

if sys.platform != "linux":
    print('WARNING: LocalCUDACluster only avliable on linux platforms. Local GPU clusters not avaliable.') 
else:
    from dask_cuda import LocalCUDACluster
    

class ADIASClusterManager():
        """
        Manages the generation and closing of clusters.
        Note: need to replace 8787 port if an open cluster is found or be safe andcd proj
        abort setup.
        """
        def __init__(self, cuda=False, remote=False, n_workers=1, worker_cores=8, 
                     worker_threads=8, worker_memory=16.0, wait_for_workers=1, adaptive=False):
            self.remote = remote
            self.cuda = cuda
            self.n_workers = n_workers
            self.worker_cores = worker_cores
            self.worker_threads = worker_threads
            self.worker_memory = worker_memory
            self.wait_for_workers = wait_for_workers
            self.gateway = None
            self.options = None
            self.dashboard_address = None
            self.adaptive = adaptive
            
        def start_cluster(self):
            # Local clusters
            if not self.remote:
                # Local CPU cluster
                if not self.cuda:
                    self.cluster = LocalCluster()
                    self.client = Client(self.cluster)
                # Local cuda cluster
                else:
                    # Only load CUDACLuster if on linux platform (assumed for ADIAS)
                    if sys.platform != "linux":
                        self.cluster = LocalCluster()
                    else:
                        self.cluster = LocalCUDACluster()
                    self.client = Client(self.cluster) 
                
                # Get local dashboard
                user = os.environ.get("JUPYTERHUB_USER")
                self.dashboard_address = f'https://hub.adias.aquawatchaus.space/user/{user}/proxy/8787/status'
                print("\nCluster Dashboard:\n"+self.dashboard_address+"\n")

            # Remote clusters
            elif self.remote:
                # Open a gateway
                self.gateway = Gateway()
                self.options = self.gateway.cluster_options()
                # Set gateway options
                self.options['worker_cores'] = self.worker_cores
                self.options['worker_threads'] = self.worker_threads
                self.options['worker_memory'] = self.worker_memory
                self.options['cuda_worker'] = self.cuda
                # Check if there are any open clusters and if not start one
                clusters = self.gateway.list_clusters()
                if not clusters:
                    print('Creating new remote cluster. Please wait..')
                    self.cluster = self.gateway.new_cluster(cluster_options=self.options)
                else:
                    print(f'An existing remote cluster was found. Connecting to: {clusters[0].name}')
                    self.cluster = self.gateway.connect(clusters[0].name)
                
                # Scale the cluster
                if self.adaptive:
                    self.cluster.adapt(minimum=1, maximum=self.n_workers)
                else:
                    self.cluster.scale(self.n_workers)
                
                # Get the client
                self.client = self.cluster.get_client()
                
                # Get the new dashboard address
                self.dashboard_address = self.cluster.dashboard_link
                print("\nCluster Dashboard:\n"+self.dashboard_address+"\n")

                # Wait for workers
                if self.wait_for_workers > 0:
                    print('Waiting for workers..')
                    self.client.wait_for_workers(n_workers=self.wait_for_workers)
        
        # Make sure everything gets shutdown
        def shutdown(self):
            if self.remote:
                print('Shutting down client and cluster')
                self.cluster.shutdown()
                self.client.close()
            else:
                print('Cluster is local, closing instead.')
                self.close()
        
        def close(self):
            if self.remote:
                print('Cluster is remote, shutting down instead.')
                self.shutdown()
            else:
                print('Closing client and cluster')
                self.cluster.close()
                self.client.close()


class ADIASFileManager():
    """
    Class to mange file IO to make it easier to change between local files
    and S3 class storage. I've modified the approach used in the EASI cookbook slightly. 
    I using the following definitions:
    bucket_name: s3 bucket
    prefix: path to project top "directory"
    path: path to requested file or directory

    If an explict s3 path is passed, bucket and prefix will be ignored. 
    
    Haven't coded in asynchronous features yet.
    Would need to have it launch a session. If it's in a jupyter notebook that needs
    to be the notebooks loop. 
    """
    def __init__(self, bucket='adias-prod-dc-data-projects', prefix='ai4m-cf/phi233/projects/riverFlow',
                 s3=False, asynchronous=False):
        self.bucket = bucket
        self.prefix = prefix
        self.s3loc = f's3://{bucket}/{prefix}'
        self.use_s3 = s3
        self.asynchronous = asynchronous
        self.s3 = s3fs.S3FileSystem(asynchronous=asynchronous)

    def check_s3(self, path):
        return(path[0:5] == 's3://')
        
    def s3_path(self, path, force=False):
        if force or (self.use_s3 and not self.check_s3(path)):
            # remove '.' and '/' for top directories
            path = path[0].replace('.','')+path[1:]
            path = path[0].replace('/','')+path[1:]
            return(os.path.join(self.s3loc, path))
        return(path)
    
    def open(self, path, *args, **kwargs):
        if self.use_s3:
            return(self.s3.open(self.s3_path(path), *args, **kwargs))
        return(open(path, *args, **kwargs))

    def os_walk(self, path, *args, **kwargs):
        if self.use_s3:
            return(self.s3.walk(self.s3_path(path), *args, **kwargs))
        return(os.walk(path, *args, **kwargs))

    def os_listdir(self, path, *args, **kwargs):
        if self.use_s3:
            files = self.s3.ls(self.s3_path(path), *args, **kwargs)
            files = [fn.split('/')[-1] for fn in files]
            return(files)
        return(os.listdir(path, *args, **kwargs))

