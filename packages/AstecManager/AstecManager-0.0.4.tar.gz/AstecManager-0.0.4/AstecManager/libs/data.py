import os


def imread(filename, verbose=True,voxel_size=False):
    """Reads an image file completely into memory

    :Parameters:
     - `filename` (str)
     - `verbose` (bool)
     - `voxel_size` (bool)

    :Returns Type:
        |numpyarray|
    """
    if verbose:
        print(" --> Read " + filename)
    if not isfile(filename):
        if verbose:
            print("Miss "+filename)
        return None
    try:

        if filename.find("mha") > 0:
            from morphonet.ImageHandling import imread as imreadINR
            data, vsize = imreadINR(filename)
            if voxel_size:
                return np.array(data), vsize
            else:
                return np.array(data)
        elif filename.find('.inr') > 0:
            from morphonet.ImageHandling import imread as imreadINR
            data,vsize = imreadINR(filename)
            if voxel_size:
                return np.array(data),vsize
            else:
                return np.array(data)
        elif filename.find('.nii') > 0:
            from nibabel import load as loadnii
            im_nifti = loadnii(filename)
            if voxel_size:
                sx, sy, sz = im_nifti.header.get_zooms()
                vsize = (sx, sy, sz)
                data = np.array(im_nifti.dataobj).astype(np.dtype(str(im_nifti.get_data_dtype())))
                #data = np.swapaxes(data,0,2)
                return data,vsize
            else :
                return data
        elif filename.find("h5") > 0:
            import h5py
            with h5py.File(filename, "r") as f:
                return np.array(f["Data"])
        else:
            from skimage.io import imread as imreadTIFF
            imtiff = imreadTIFF(filename)
            imtiff = np.swapaxes(imtiff,0,2)
            if voxel_size:
                vsize = TIFFTryParseVoxelSize(filename)
                return imtiff,(float(vsize[0]), float(vsize[1]), float(vsize[2]))
            else:
                return imtiff
    except Exception as e:
        if verbose:
            print(" Error Reading " + filename)
            print(str(e))
            if filename.endswith("gz") or filename.endswith("zip"):
                temp_path = "TEMP" + str(time.time())
                while os.path.isdir(temp_path):  # JUST IN CASE OF TWISE THE SAME
                    temp_path = "TEMP" + str(time.time())
                os.system("mkdir -p " + temp_path)
                os.system("cp " + filename + " " + temp_path)
                filename = join(temp_path, os.path.basename(filename))
                os.system("gunzip " + filename)
                filename = filename.replace('.gz', '')
                if voxel_size:
                    arrayim,vsize = imread(filename,verbose,voxel_size)
                    if temp_path is not None:
                        os.system("rm -rf " + temp_path)
                    return arrayim,vsize
                else :
                    arrayim = imread(filename,verbose,voxel_size)
                    if temp_path is not None:
                        os.system("rm -rf " + temp_path)
                    return arrayim

            return None
        # quit()
    return None
class Cell:
    id = -1
    t = -1
    mothers = []
    daughters = []

    def __init__(self,id_cell,time_cell):
        self.id = id_cell
        self.t = time_cell
        self.mothers = []
        self.daughters = []

    def add_mother(self,cell):
        #print("mother len before : " + str(len(self.mothers)))
        #print("add mother for cell : "+str(self.t)+","+str(self.id)+" for mother : "+str(cell.t)+","+str(cell.id))
        if self.mothers is None:
            self.mothers = []
        if not cell in self.mothers:
            self.mothers.append(cell)
        #print("mother len after : " + str(len(self.mothers)))
        cell.add_daughter(self)


    def add_daughter(self,cell):
        #print("daughters len before : " + str(len(self.daughters)))
        #print("add daughter for cell : " + str(self.t) + "," + str(self.id) + " for mother : " + str(cell.t) + "," + str(cell.id))
        if self.daughters is None:
            self.daughters = []
        if not cell in self.daughters:
            self.daughters.append(cell)

def is_image(imagepath):
    """
        Returns true if file is a readable image or not

        Parameters
        --------
        path : basestring
            Path to file to test
        Returns
        --------
        boolean
            is file image or not
    """
    return os.path.isfile(imagepath) and (imagepath.endswith(".mha") or imagepath.endswith(".nii") or imagepath.endswith(".inr") or imagepath.endswith(".mha.gz") or imagepath.endswith(".nii.gz") or imagepath.endswith(".inr.gz"))

def get_id_t(idl):
    """ Return the cell t,id

            Parameters
            ----------
            idl : int
                Cell information id
            Returns
            -------
            t : int
                Cell time point
            id : int
                Cell id
    """
    t=int(int(idl)/(10**4))
    cell_id=int(idl)-int(t)*10**4
    return t,cell_id

def get_longid(t,idc):
    """ Return the cell information id

            Parameters
            ----------
            t : int
                Cell time point
            idc : int
                Cell id

            Returns
            -------
            id : int
                Cell information id format {ttt0iiii}
    """
    if t==0 or  t=="0":
        return idc
    return t*10**4+idc

