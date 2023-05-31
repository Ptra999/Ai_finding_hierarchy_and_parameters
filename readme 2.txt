

To execute the program, run the following command:
    $ python bnet.py [required-parameters] [given [on-given-parameters]]

Example:
    $ python bnet.py Jf given Et Bf

Note:
- 'given' should be in lower case
- All terms should start with upper case 'X' and end with lower case
- The Upper case of term represents events, where 
    'A' - Alarm
    'B' - Burglary
    'E' - Earthquake
    'M' - Mary Calls
    'J' - John Calls
- and the Lower case of term represents happening in boolean. Like:
    't' - True
    'f' - False
- consider that the term is 'Af' it means Event 'Alarm Rings did not happen'
- required-parameters and on-given-parameters are collection of terms seperated by space