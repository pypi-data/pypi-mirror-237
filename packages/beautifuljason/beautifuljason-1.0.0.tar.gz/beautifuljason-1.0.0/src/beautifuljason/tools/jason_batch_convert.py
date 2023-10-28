##
##-----------------------------------------------------------------------------
##
## Copyright (c) 2023 JEOL Ltd.
## 1-2 Musashino 3-Chome
## Akishima Tokyo 196-8558 Japan
##
## This software is provided under the MIT License. For full license information,
## see the LICENSE file in the project root or visit https://opensource.org/licenses/MIT
##
##++---------------------------------------------------------------------------
##
## ModuleName : BeautifulJASON
## ModuleType : Python API for JASON desktop application and JJH5 documents
## Purpose : Automate processing, analysis, and report generation with JASON
## Author : Nikolay Larin
## Language : Python
##
####---------------------------------------------------------------------------
##

import os
from multiprocessing import Pool

def do_conversion(fname, jason, args):
    base_name = os.path.splitext(fname)[0]
    out_fnames = [os.path.join(args.out_dir, base_name + '.' + format) for format in args.formats]
    jason.save(os.path.join(args.in_dir, fname), out_fnames)
    print(fname, "- done")

def main():
    import argparse
    import datetime
    from pathlib import Path

    import beautifuljason as bjason

    parser = argparse.ArgumentParser(description='Convert files from a specified directory.')
    parser.add_argument('in_dir', help='Directory containing files to be converted.')
    parser.add_argument('out_dir', help='Directory where the converted files will be saved.')
    parser.add_argument('-formats', help='List of desired output file formats. Multiple formats can be specified.', 
                        nargs='+', required=True, choices=['jjh5', 'jjj', 'jdx', 'jdf', 'pdf', 'png', 'jpg', 'svg'])
    parser.add_argument('-extensions', help='List of file extensions to convert. For example: jdf 1 jdx.', 
                        nargs='+', required=True)
    args = parser.parse_args()

    # Initialize Jason
    jason = bjason.JASON()

    # Create output directory
    Path(args.out_dir).mkdir(parents=True, exist_ok=True)

    # Multithreaded conversion
    fnames = [f for f in os.listdir(args.in_dir) if os.path.splitext(f)[1][1:] in args.extensions]
    print(len(fnames), "files found.")
    start_time = datetime.datetime.now()
    print("Started at:", start_time)
    print("Please be patient. Due to multithreading, the computer may slow down while the conversion is in progress.")
    with Pool() as p:
        p.starmap(do_conversion, zip(fnames, [jason]*len(fnames), [args]*len(fnames)))
    end_time = datetime.datetime.now()
    print("Finished at:", end_time)
    print("Duration:", end_time - start_time)

if __name__ == '__main__':
    main()
