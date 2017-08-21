#!/bin/bash
set -e

cd docker-mpv
git pull
rpmdev-setuptree
cp mpv.spec /root/rpmbuild/SPECS/
cd /root/rpmbuild/SOURCES/
wget $(awk '/Source/ {print $2}' ../SPECS/mpv.spec)
cd ..
rpmbuild -bb SPECS/mpv.spec
cp -f RPMS/x86_64/mpv*.rpm /output/
