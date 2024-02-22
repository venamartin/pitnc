# Digipeater with PiTNC

1. `ssh` into the PiTNC and modify the contents of the file `direwolf.conf`. You might want to make a backup first by `cp ~/direwolf.conf ~/direwolf.conf.bak`.
    ```console
    ssh tnc@pitnc.local
    nano ~/direwolf.conf
    ```

1. Find **MYCALL** and change to your callsign:
    ```
    MYCALL YOURCALLSIGN
    ```

1. Find the line `#DIGIPEAT ...` and remove the comment

    ```
    DIGIPEAT 0 0 ^WIDE[3-7]-[1-7]$|^TEST$ ^WIDE[12]-[12]$ TRACE
    ```
    
    If you wanted a "fill-n" digi, that responded to only WIDE1-1, you could use this:

    ```
    DIGIPEAT 0 0 ^WIDE1-1$ ^WIDE1-1$
    ```

1. [Optional] Configure the filtering. In this example we only digipeat position data and messages:

    ```
    FILTER t/pm
    ```

1. Restart Direwolf for the changes to take:

    ```console
    pitnc --drestart
    ```

    
