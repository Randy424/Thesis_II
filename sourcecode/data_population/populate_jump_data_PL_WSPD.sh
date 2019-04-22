#!/bin/bash

files=("/Net/samosproc/data/public/research/WTDL/2012/WTDL_20121212v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2011/WTDL_20110527v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2011/WTDL_20110528v30001.nc"
"/Net/samosproc/data/public/research/WTDL/2011/WTDL_20110731v30001.nc"
"/Net/samosproc/data/public/research/NEPP/2010/NEPP_20100919v30001.nc"
"/Net/samosproc/data/public/research/NEPP/2010/NEPP_20100829v30001.nc"
"/Net/samosproc/data/public/research/NEPP/2009/NEPP_20090913v30001.nc"
"/Net/samosproc/data/public/research/NEPP/2009/NEPP_20090820v30001.nc"
"/Net/samosproc/data/public/research/NEPP/2009/NEPP_20090814v30001.nc"
"/Net/samosproc/data/public/research/NEPP/2008/NEPP_20080318v30001.nc")

for i in ${files[*]}; do
    scp rbrunopiverger@login.coaps.fsu.edu:${i} "/Users/randybrunopiverger/Documents/Daily/Thesis II/Thesis_II_Repo/data/jump_data_PL"

done 
exit 0
