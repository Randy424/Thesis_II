#!/bin/bash

files=("/Net/samosproc/data/public/research/NEPP/2010/NEPP_20100523v30001.nc"
"/Net/samosproc/data/public/research/NEPP/2009/NEPP_20090318v30001.nc"
"/Net/samosproc/data/public/research/NEPP/2009/NEPP_20091003v30001.nc"
"/Net/samosproc/data/public/research/WBP3210/2012/WBP3210_20121209v30001.nc"
"/Net/samosproc/data/public/research/WCX7445/2011/WCX7445_20110831v30001.nc"
"/Net/samosproc/data/public/research/WCX7445/2010/WCX7445_20100409v30001.nc"
"/Net/samosproc/data/public/research/WCX7445/2010/WCX7445_20100210v30201.nc"
"/Net/samosproc/data/public/research/WCX7445/2010/WCX7445_20100210v30101.nc"
"/Net/samosproc/data/public/research/WTEA/2017/WTEA_20170924v30001.nc"
"/Net/samosproc/data/public/research/WTEB/2010/WTEB_20101117v30001.nc")

for i in ${files[*]}; do
    scp rbrunopiverger@login.coaps.fsu.edu:${i} "/Users/randybrunopiverger/Documents/Daily/Thesis II/Thesis_II_Repo/data/jump_data_RH"

done 
exit 0
