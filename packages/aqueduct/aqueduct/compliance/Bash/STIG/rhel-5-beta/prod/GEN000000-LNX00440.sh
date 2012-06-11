#Aqueduct - Compliance Remediation Content
#Copyright (C) 2011,2012  Vincent C. Passaro (vincent.passaro@gmail.com)
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor,
#Boston, MA  02110-1301, USA.

#!/bin/bash
######################################################################
#By Tummy a.k.a Vincent C. Passaro				     #
#Vincent[.]Passaro[@]gmail[.]com	         		     #
#www.vincentpassaro.com						     #
######################################################################
#_____________________________________________________________________
#|  Version |   Change Information  |      Author        |    Date    |
#|__________|_______________________|____________________|____________|
#|    1.0   |   Initial Script      | Vincent C. Passaro | 20-oct-2011|
#|	    |   Creation	    |                    |            |
#|__________|_______________________|____________________|____________|
#
#
#  - Updated by Shannon Mitchell (shannon.mitchell@fusiontechnology-llc.com)
# on 28-dec-2011 to check the permissions before running the chmod command.
# And changed the chmod to allow for "less permissive" permissions.

								     

#######################DISA INFORMATION###############################
#Group ID (Vulid): V-1055
#Group Title: Access File Permissions
#Rule ID: SV-1055r5_rule
#Severity: CAT II
#Rule Version (STIG-ID): GEN000000-LNX00440
#Rule Title: The /etc/security/access.conf file must have mode 0640 or 
#less permissive.
#
#Vulnerability Discussion: If the access permissions are more permissive 
#than 0640, system security could be compromised.
#
#Responsibility: System Administrator
#IAControls: ECLP-1
#
#Check Content: 
#Check access configuration mode:
#
# ls -lL /etc/security/access.conf
#
#If this file exists and has a mode more permissive than 0640, this 
#is a finding.
#
#Fix Text: Use the chmod command to set the permissions to 0640.
#For example:
# chmod 0640 /etc/security/access.conf   
#######################DISA INFORMATION###############################

#Global Variables#
PDI=GEN000000-LNX00440

#Start-Lockdown

if [ -a "/etc/security/access.conf" ]
  then

    # Pull the actual permissions
    FILEPERMS=`stat -L --format='%04a' /etc/security/access.conf`

    # Break the actual file octal permissions up per entity
    FILESPECIAL=${FILEPERMS:0:1}
    FILEOWNER=${FILEPERMS:1:1}
    FILEGROUP=${FILEPERMS:2:1}
    FILEOTHER=${FILEPERMS:3:1}

    # Run check by 'and'ing the unwanted mask(7137)
    if [ $(($FILESPECIAL&7)) != "0" ] || [ $(($FILEOWNER&1)) != "0" ] || [ $(($FILEGROUP&3)) != "0" ] || [ $(($FILEOTHER&7)) != "0" ]
      then
        chmod u-xs,g-wxs,o-rwxt /etc/security/access.conf
    fi
  else
    echo "------------------------------" > $PDI-error.log
    date >> $PDI-error.log
    echo " " >> $PDI-error.log
    echo "/etc/security/access.conf does not exist." >> $PDI-error.log
    echo "Could not change permissions to 0640" >> $PDI-error.log
    echo "------------------------------" >> $PDI-error.log
fi


