# fapple
iTunes encrypted backup brute force password checker

This tool automates checking a list of passwords for the iTunes encrypted backup password, with a license restricting use
solely to phones that are owned by the user.  I had to write it, because Apple's encrypted backup feature suffers a design flaw.  

The encryption process they built, uses a database on the iphone.  Once you turn the iTunes encryption feature on,
if you forget your password, it doesn't just render your old backups useless (like it should), it forces any new backups
to exclusively be a) encrypted and b) use the old, forgotten, password.  Reseting this, requires a 
[device wipe](https://support.apple.com/en-ca/HT203790), or jailbreaking.  Which, is rediculous, 
because what person **wouldn't want to make a backup before wiping their device?**

The good news, is that this wasn't the only flaw in their design.  Their password checking tool, also suffers a flaw.
It will let you try infinite passwords. 

## Barely complete!

I wrote this tool, in less than an hour and a single commit. So, it's barely complete.  
But, it's functional and worked for me.  It found my password after trying a list of 
960 possible passwords which I gave (read: I had knowledge of permutations about my own passwords)
it to start with.

### Incomplete Virtual Keyboard Map
This process took a material amount of time, but it worked.  The virtual keyboard map is an incomplete
dictionary.  The dictionary needs to be completed, for this tool to work on passwords with non-alpha numeric symbols.
I'll complete the dictionary, if somebody paypals $200 to jeffrey.mclarty@gmail.com.

### Timings
The timings are sloppy.  They could be tightened up.  Like I said; I wrote this tool in less than an hour.

## Usage

1. Have a list of passwords you want to try, assign them to the candidates variable in passlist.py
2. Assign something to the newpassword variable in bforcer.py
3. Turn on itunes.
4. Calibrate mouse positions.
    Use getcurpos.py to get the x & y coordinates of thethree buttons and one text field, 
    in iTunes that one would click while trying a password.  
    
    Set them, in bforcer.py.  The four variables are:
    
    * ChangePassworddotdotdot
    * ChangePassword
    * OK
    * OldPassword
5. Run bforcer.py
6. Wait. 

## Support?

This tool is unsupported.  See the license.  Don't e-mail me unless you have lots of money and will give me some.

## License

This software uses a four-clause adaptation of BSD three-clause, as detailed below.

Copyright (c) 2015, Jeffrey McLarty
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of fapple nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.
  
* This sofware may only be used on iPhone devices and their associated
  iTunes backup software, if both are owned and controlled by the user.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

