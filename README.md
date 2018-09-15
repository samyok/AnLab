# Fixing Perl Scripts
This is a project undertaken by Samyok Nepal to see if he can fix/update old Perl scripts from a long time ago.
## `config.json`
There should be a `config.json` that ships with this test data, make sure that it is in the same location as the scripts. 
## Directories
Each data file and python program must go in a specific spot, and can be customized in `config.json`.
### Data Dir
    test_data/
    ├── CGIs_mapped.txt
    ├── test_CGIs_high.txt
    ├── test_CGIs_low.txt
    ├── test_CGI.txt
    └── test_methlyation.txt
    
### Programs
Here is the flow of the data through the programs. This uses the `config.json` property values without `INPUT`/`OUTPUT`.
 
                METHLYATION_FILE ───┐
                CGI_FILE ─┬─────────┤
                 ┌────────┘ ┌───────┘
                 │          │
                 │    CGImapper.py >>> CGI_MAP ───┐
                 │                                │
                 │          ┌─────────────────────┘
                 │          │
                 │   high_low_split.py >>> CGIs_HIGH ───┐
                 │          └───────── >>> CGIs_LOW ────┤
                 │                                      │
                 └────┬─────────────────────┬───────────┘
                      │                     │
    PAIRS <<< CGI_pair_finder.py   Single_CGI_finder.py >>> CGIs_HIGH_SINGLE     
      │                                     └────────── >>> CGIs_LOW_SINGLE      
                  
                                                      
    I can't find a script that takes
        these files as input
## Packages needed
I wrote a mini-package for this project--it should come zipped with the programs and test data. 
### Package Documentation
#### Classes
1. `CGI`: An island

|Method|Params|
|-----|----|
|Constructor| - `line`: A line formatted in the same way as test_CGI.txt |

|Attributes|Description|
|---|---|
|start| Where the CGI starts|
|end  | Ending point | 
|number| Number of CPGs in CG-Island|


I started writing the classes in the beginning of the project, but it turned out that I actually didn't need them for most programs.	
