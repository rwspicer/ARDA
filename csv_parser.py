"""
csv_parser.py
ARDA
Ross Spicer
2015/02/28

    parses & prepares the resources, provided by the ASA, for input 
into mysql database. 

"""


def parse_file(f_name):
    """
    this function parses a csv file to remove blank lines
    
    arguments:
        f_name:     a cav text file
    """
    myfile = open(f_name, 'r')
    rows = myfile.read().split('\n')
    cells = []
    for line in rows:
        if line == '' or line[0] == '\t':
            continue
        cells.append(line.split('\t'))
    return cells


def process_lib(grid):
    """
        this function is to remove extranuous data from the physical libaray 
    listings for the arda project
    
    arguments:
        grid = a grid of text cells, (a list of rows of cells)
    """
    p_grid = [] 
    for line in grid:
        if len(line) != 5:
            print len(line)
            print line
            continue
        try:  
            int(line[0])
        except ValueError:
            continue
        p_grid.append(line)
    return p_grid
            
            
def process_org(grid):
    """
        this function is to remove extranuous data from the orginazation 
    listings for the arda project
    
    arguments:
        grid = a grid of text cells, (a list of rows of cells)
    """
    return grid[1:]
       
       
def print_grid(grid):
    """
        this function prints a grid 
    """
    for row in grid:
        print row
    
