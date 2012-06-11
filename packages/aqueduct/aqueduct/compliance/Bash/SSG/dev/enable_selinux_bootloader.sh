#!/bin/bash
# 
# Copyright (c) 2010, 2011 Tresys Technology LLC, Columbia, Maryland, USA
#
# This software was developed by Tresys Technology LLC
# with U.S. Government sponsorship.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# If it isn't installed, it can't be configured
[ -f /boot/grub/grub.conf ] || exit 1

egrep -q '(enforcing|selinux)=0' /boot/grub/grub.conf
[ $? -ne 0 ] && exit 0

sed -i -re 's/(enforcing|selinux)=0/ /g' /boot/grub/grub.conf

