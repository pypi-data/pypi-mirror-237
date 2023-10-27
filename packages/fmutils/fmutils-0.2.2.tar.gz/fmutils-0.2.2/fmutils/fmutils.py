
import re, os, shutil, sys
import numpy as np
from tqdm import tqdm, trange
import pathlib
from pathlib import Path
from sklearn.model_selection import train_test_split

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def get_all_files(main_dir, sort=True):
    '''
    Parameters
    ----------
    main_dir : string/path
        Absolute/relative path to root directory containing all files.
    sort : Bool, optional
        Whether to sort the output list of files or not. The default is True.

    Returns
    -------
    file_list : List
        List containing full paths of all the files.

    '''
    file_list = []
    for root, dirs, files in os.walk(main_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    if sort:
        file_list = sorted(file_list, key=numericalSort)

    return file_list


def get_all_dirs(main_dir, sort=True):
    '''
    Parameters
    ----------
    main_dir : string/path
        Absolute/relative path to root directory containing all sub-dirs.
    sort : Bool, optional
        Whether to sort the output list of dirs or not. The default is True.

    Returns
    -------
    file_list : List,
        List containing full paths of all the dirs.

    '''
    dir_list = []
    for root, dirs, files in os.walk(main_dir):
        for dr in dirs:
            dir_list.append(os.path.join(root, dr))
    if sort:
        dir_list = sorted(dir_list, key=numericalSort)

    return dir_list


def get_num_of_files(main_dir):
    '''
    Parameters
    ----------
    main_dir : string/path
        Absolute/relative path to root directory containing all files.
    
    Returns
    -------
    A Dictionary containing follwoing keys/info.
    files_in_sub_dirs : an array containing number of file in all sub dirs of root.
    sub_dirs : name of all the sub-dirs/classes inside the root.
    total_files : total number of files in all the sub-dir/classes.
    
    '''   
    file_count = []
    for root, dirs, files in os.walk(main_dir):
        file_count.append((os.path.basename(os.path.normpath(root)), len(files)))
    
    if len(file_count) > 1: # if the main_dir have sub_dirs
        file_count = file_count[1:]
        
        name_classes = np.asarray(file_count)[:,0].astype(str)
        num_per_class = np.asarray(file_count)[:,1].astype(int)
        
        total_files = sum(num_per_class)
        
        dir_prop = {'sub_dirs':name_classes, 'files_in_sub_dirs':num_per_class,
                    'total_files':total_files}
    else: # if the main_dir don't have sub_dirs
        total_files = file_count[0][1]
        
        dir_prop = {'sub_dirs':None, 'files_in_sub_dirs':None,
                    'total_files':total_files}
    
    return dir_prop


def get_basename(full_path):
    '''
    Parameters
    ----------
    full_path :  string/path
        Absolute path to the file.

    Returns
    -------
    name : string
        basename of the file.

    '''
    return Path(full_path).stem

def get_suffix(full_path):
    '''
    Parameters
    ----------
    full_path :  string/path
        Absolute path to the file.

    Returns
    -------
    name : string
        extension of that file.

    '''
    return Path(full_path).suffix

def get_pdir(full_path):
    '''
    Parameters
    ----------
    full_path :  string/path
        Absolute path to the file.

    Returns
    -------
    name : string
        parent dir/sub-dir containing file.

    '''
    return Path(full_path).parent.name

def get_random_files(main_dir, count=1):
    '''
    
    Parameters
    ----------
    main_dir : path/string
        Absolute/relative path to root directory containing all files.
    count : int, optional
        Total numbner of randomly selected files. The default is 1.

    Returns
    -------
    file_path : list
        A list containig full paths to randomly selected files.

    '''
    file_list = get_all_files(main_dir, sort=True)
    file_path = np.random.choice(file_list, size=count, replace=False)
    
    return file_path


def del_all_files(main_dir, confirmation=True):
    '''
    
    Parameters
    ----------
    main_dir : path/string
        Absolute/relative path to root directory containing all files to be deleted.
    confirmation : Bool, optional
        Whether to ask for confirmation before deleting all the files. The default is True.

    Returns
    -------
    None.
    
    Warning
    -------
    If you set the confirmation to False then all the files inside the root directory 
    will be permanently deleted.

    '''
    file_list = get_all_files(main_dir, sort=True)
    if confirmation:
        ans = input(f'do you wnat to continue deleting {len(file_list)} files? [yes[y]/no[n]] \n')
    else:
        ans = 'y'
    if ans == 'y':
        for i in file_list:
            os.remove(i)
        n = len(file_list)
        print(f'{n} files deleted.')
    else:
        print('Operation stopped.')
    return

def split_some_data(origin_dir, dest_dir, split=0.3, move=False):
    '''
    Note
    ----------
    Copies a portion of data to a new 'dest_dir'.
    
    Parameters
    ----------
    origin_dir : origin dir which contains all the sub dirs having all files.
    dest_dir : destination dir where to put the splitted data.
    split : Float between [0, 1], percentage of data to split. The default is 0.3.
    move : if True the selected files will be moved to the new dir (not copied.)
    
    Returns
    -------
    None. 
    '''
    origin_dir = origin_dir +'/'
    dest_dir = dest_dir +'/'
    
    class_dirs = get_all_dirs(origin_dir)
    
    # making dirs in the destination dir first so we can copy/move files there.
    dirs = os.listdir(origin_dir)
    for i in dirs:
        try:
            os.mkdir(dest_dir + i)
        except FileExistsError:
            pass
    class_dests = get_all_dirs(dest_dir)
    
    for class_dir, class_dest in tqdm(zip(class_dirs, class_dests), desc='Splitting Data', total=len(class_dirs)):
        
        files = get_all_files(class_dir)
        portion = int(len(files) * split)
        files_to_move = get_random_files(class_dir, count=portion)
        for file in files_to_move:
            name = os.path.basename(file)
            if move:
                shutil.move(file, os.path.join(class_dest, name))
            else:
                shutil.copy2(file, class_dest)
    
    return

def clone_dir_tree(source_dir, dest_dir):
    '''
    
    Parameters
    ----------
    source_dir : string/path
        dir form which to clone the dir tree.
    dest_dir : string/path
        base dir location where the new dir tree will be cloned
    
    Returns
    -------
    None. Creates the directories at new location without copying files
    '''
    x = get_all_dirs(source_dir)
    
    dirs = []
    [dirs.append(x[j].split('/')[-1]) for j in range(len(x))]
    
    for i in dirs:
        try:
            os.mkdir(dest_dir + i)
        except FileExistsError:
            pass
    print(f'Cloned {len(x)} directories and sub-directories in total.')
    return


def file_name_replacer(main_dir, new_name, name2replace):
    '''
    
    Parameters
    ----------
    data_dir : string/path
        main dir containig all the sub dir.
    new_name : list of strings
        A list containing the new names which will replace the old ones.
    name2replace : list of string
        A list containing the strings which will be replaced wiht new ones.

    Returns
    -------
    None.

    Note
    -------
    Changes the names of all files inside a dir by replacing the specific strings
    in old file name with new ones, specified via 2 input lists.
    Both lists should have same length
    '''
    full_paths = get_all_files(main_dir + '/')
    
    k_name = name2replace
    e_name = new_name
    
    new_full_paths = []
    
    for i in full_paths:
        name = os.path.basename(i)
        for j in range(len(k_name)):        
            temp = name.replace(k_name[j], e_name[j])
            name = temp
        #new_names.append(name)
        
        new_full_paths.append(os.path.join(os.path.dirname(i), name)) 
    [os.rename(full_paths[c], new_full_paths[c]) for c in range(len(full_paths))]
    
    return
    
def rename_wrt_dirname(main_dir):
    
    '''
    Note
    ----------
    Change the names of all files inside the main_dir wrt their sub_dir names.
    
    Parameters
    ----------
    main_dir :  string/path
        main directory containing all sub dirs.
    
    Returns
    -------
    None.
    
    '''
    main_dir = main_dir +'/'
    x = get_all_files(main_dir)
    
    for i in trange(len(x), desc="Changing names of files"):
        ext_name = os.path.basename(x[i]).split('.')[-1]
        if sys.platform == 'linux':
            new_name = os.path.dirname(os.path.normpath(x[i])).split('/')[-1]
        else: #windows
            new_name = os.path.dirname(os.path.normpath(x[i])).split('\\')[-1]
        
        new_full_path = os.path.dirname(os.path.normpath(x[i]))+'/' + \
                        f'{new_name}_{i:03d}.' + ext_name
    
    
        os.rename(x[i],
                  os.path.join(os.path.dirname(x[i]), new_full_path))
    
    return

def move_matching_files(path2copy, path2match, path2paste):
    '''
    
    Parameters
    ----------
    path2copy : string/path
         Absolute path to directory from where to copy files.
    path2match : string/path
        Absolute path to directory from where to match files/file-names.
    path2paste : string/path
        Absolute path to directory where to move the files having matched names.

    Returns
    -------
    None.
    
    Note
    -------
    Example use case might be in your ML training data you have labels in one dir and
    images in one dir but you deleted some blurred/damages images and now you only want 
    to keep labels that have their corresponding images.
    '''
    #we shall store all the file names in this list
    all_filelist = []
    
    
    for root, dirs, files in os.walk(path2copy, topdown=False):
    	for file in files:
            #append the file name to the list
    		all_filelist.append(os.path.join(root,file))
    
    file_names = os.listdir(path2match)
    for i in range(len(file_names)):
        file_names[i] = get_basename(file_names[i], include_extension=False) # remove extension of label files 
    
    all_file_names = [os.path.basename(c) for c in all_filelist]
    for i in range(len(all_file_names)):
        all_file_names[i] = get_basename(all_file_names[i], include_extension=False) # remove extension of original data
    
    ids = []
    
    for j in range(len(file_names)):
        try:
            x = all_file_names.index(file_names[j])
            ids.append(x)
        except ValueError:
            #print('Error')
            pass
    
    print(f'{len(ids)} mathcing files found out of {len(all_filelist)}.')
    
    
    for k in tqdm(ids, desc='Copying', total=len(ids)):
        shutil.copy2(all_filelist[k], path2paste)
    return None


def tvt_split(img_dir, dest_dir, lbl_dir=None, test_split=0.2, val_split=0.1, mode='copy', multi_class=True):
    '''
    Parameters
    ----------
    img_dir : string/path
            absolute/relative path to root directory containing all files.
    dest_dir : string/path
            absolute/relative path to root directory containing all files..
    lbl_dir : TYPE
        DESCRIPTION.
    test_split : float beween [0, 1], optional
            Percentage of test split. The default is 0.2.
    val_split : TYPE, optional
        Percentage of validation split. The default is 0.1.
    mode : string, optional One of ['copy', 'move']
        Whether to copy the data or move it. The default is 'copy'.
    multi_class : boolean,
        Whether their are multiple classes in data or only one class.
        
    Returns
    -------
    None.
    
    Note
    -------
    Create Train-Validation-Test splits of the data for ML models. in follwoing format
    
    ../split/
    │
    ├── test\
    │   └── images\
    │       ├── class_1\
    │       │
    │       ├── class_2\
    ├── train\
    │   └── images\
    │       ├── class_1\
    │       │
    │       ├── class_2\
    └── val\
        └── images\
            ├── class_1\
            │
            ├── class_2\

    '''
    test_data = test_split
    val_data = val_split
    
    mode = mode
    
    img_paths = get_all_files(img_dir)
    if lbl_dir != None:
        #print('Lables will also be copied.')
        mask_paths = get_all_files(lbl_dir)
     
    
    if lbl_dir == None:
        x_train_val, x_test = train_test_split(img_paths, test_size=test_data, random_state=42)
    
        x_train, x_val = train_test_split(x_train_val, test_size=val_data, random_state=42)
    else:
        x_train_val, x_test, y_train_val, y_test = train_test_split(img_paths, mask_paths,
                                                                    test_size=test_data, random_state=42)
        
        x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val,
                                                                    test_size=val_data, random_state=42)
    
    x = len(img_paths)
    print(f'{30*"*"} \n Total {x} images found. \n\
          Train Data = {len(x_train)} \n\
          Test Data = {len(x_test)} \n\
          Val Data = {len(x_val)}\n{30*"*"}')
          
    img_data = [x_train, x_test, x_val]
    if lbl_dir != None:
        label_data = [y_train, y_test, y_val]
    
    sub_dir = ['train', 'test', 'val']
    
    for i in sub_dir:
            try:
                os.mkdir(dest_dir + i)
                os.mkdir(dest_dir + i + '/images/')
                clone_dir_tree(img_dir, dest_dir + i + '/images/')
                if lbl_dir != None:
                    os.mkdir(dest_dir + i + '/lbls/')
                    clone_dir_tree(img_dir, dest_dir + i + '/lbls/')
            except FileExistsError:
                pass
            
    for i in range(len(sub_dir)):
        im_path = os.path.join(dest_dir, sub_dir[i] + '/images/')
        if lbl_dir != None:
            ms_path = os.path.join(dest_dir, sub_dir[i] + '/lbls/')
        
        if lbl_dir != None:
            for j,k in tqdm(zip(img_data[i],label_data[i]), desc=f'Creating {sub_dir[i]} set', total=len(img_data[i])):
                if multi_class:
                    cls_dir = os.path.dirname(j).split('/')[-1]
                else:
                    cls_dir = ''
                if cls_dir != os.path.dirname(img_dir).split('/')[-1]:
                    final_img_path = os.path.join(im_path, cls_dir)
                    if lbl_dir != None:
                        final_mask_path = os.path.join(ms_path, cls_dir)
                # print(im_path)
                # print(final_img_path)
                # print(cls_dir)
                if mode == 'copy':
                    shutil.copy2(j, final_img_path)
                    shutil.copy2(k, final_mask_path)
                if mode == 'move':
                    shutil.move(os.path.normpath(j), os.path.normpath(final_img_path))
                    shutil.move(os.path.normpath(k), os.path.normpath(final_mask_path))
        else:
            for j in tqdm(img_data[i], desc=f'Creating {sub_dir[i]} set', total=len(img_data[i])):
                
                cls_dir = os.path.dirname(j).split('/')[-1]
                if cls_dir != os.path.dirname(img_dir).split('/')[-1]:
                    final_img_path = os.path.join(im_path, cls_dir)
                    # if lbl_dir != None:
                    #     final_mask_path = os.path.join(ms_path, cls_dir)
                        
                if mode == 'copy':
                    shutil.copy2(os.path.normpath(j), os.path.normpath(final_img_path))
                if mode == 'move':
                    shutil.move(os.path.normpath(j), os.path.normpath(final_img_path))
    
    return None


def remove_empty_dirs(main_dir):
    '''
    
    Parameters
    ----------
    main_dir : string/path
         Absolute path to directory from where you want to remove all the empty directories.

    Returns
    -------
    None.
    '''
    walk = list(os.walk(main_dir))
    for path, _, _ in walk[::-1]:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)
    return None

def get_dir_props(main_dir):
    '''
    Parameters
    ----------
    main_dir : absolute/relative path to root directory containing all files.
    
    Returns
    -------
    A Dictionary containing follwoing keys/info;
    files_in_sub_dirs : an array containing number of file in all sub dirs of root.
    sub_dirs : name of all the sub-dirs/classes inside the root.
    total_files : total number of files in all the sub-dir/classes.
    
    '''   
    file_count = []
    for root, dirs, files in os.walk(main_dir):
        file_count.append((os.path.basename(os.path.normpath(root)), len(files)))
    
    if len(file_count) > 1: # if the main_dir have sub_dirs
        file_count = file_count[1:]
        
        name_classes = np.asarray(file_count)[:,0].astype(str)
        num_per_class = np.asarray(file_count)[:,1].astype(int)
        
        total_files = sum(num_per_class)
        
        dir_prop = {'sub_dirs':name_classes, 'files_in_sub_dirs':num_per_class,
                    'total_files':total_files}
    else: # if the main_dir don't have sub_dirs
        total_files = file_count[0][1]
        
        dir_prop = {'sub_dirs':None, 'files_in_sub_dirs':None,
                    'total_files':total_files}
    
    return dir_prop