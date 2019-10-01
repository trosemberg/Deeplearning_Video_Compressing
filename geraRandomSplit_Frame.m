function geraRandomSplit_Frame(frame_number, width, height)

filename = ['bypassdecision_frame_' num2str(frame_number) '.txt'];

fid = fopen(filename, 'w');

for (h = 0:64:(height-1))
    for (w = 0:64:(width - 1))
        str = geraRandomSplitForCU(h, w, width, height);
        disp(['CU (' num2str(h) ',' num2str(w) ') - ' str])
        fprintf(fid,'CU (%4d,%4d) - %s\n',h, w, str);
        
    end
end

fclose(fid);

function str = geraRandomSplitForCU(pelY, pelX, width, height)


%Checks if this CU fits in the frame.
split_D0 = getRandomSplitForCU(pelY, pelX, 0, width, height);
str = split_D0;

%If this is split, then gets the split for the 4 children.
if (split_D0 == '1')
    split0_D1 = getRandomSplitForCU(pelY     , pelX     , 1, width, height);
    split1_D1 = getRandomSplitForCU(pelY     , pelX + 32, 1, width, height);
    split2_D1 = getRandomSplitForCU(pelY + 32, pelX     , 1, width, height);
    split3_D1 = getRandomSplitForCU(pelY + 32, pelX + 32, 1, width, height);

    str = [str ' ' split0_D1 ' ' split1_D1 ' ' split2_D1 ' ' split3_D1];
    
    %Checks each children at the depth 2
    if (split0_D1 == '1')
        split0_D2 = getRandomSplitForCU(pelY     , pelX     , 2, width, height);
        split1_D2 = getRandomSplitForCU(pelY     , pelX + 16, 2, width, height);
        split2_D2 = getRandomSplitForCU(pelY + 16, pelX     , 2, width, height);
        split3_D2 = getRandomSplitForCU(pelY + 16, pelX + 16, 2, width, height);

        str = [str ' ' split0_D2 ' ' split1_D2 ' ' split2_D2 ' ' split3_D2];
    end
    
    if (split1_D1 == '1')
        split4_D2 = getRandomSplitForCU(pelY     , pelX + 32, 2, width, height);
        split5_D2 = getRandomSplitForCU(pelY     , pelX + 48, 2, width, height);
        split6_D2 = getRandomSplitForCU(pelY + 16, pelX + 32, 2, width, height);
        split7_D2 = getRandomSplitForCU(pelY + 16, pelX + 48, 2, width, height);

        str = [str ' ' split4_D2 ' ' split5_D2 ' ' split6_D2 ' ' split7_D2];
    end
    
    if (split2_D1 == '1')
        split8_D2  = getRandomSplitForCU(pelY + 32, pelX     , 2, width, height);
        split9_D2  = getRandomSplitForCU(pelY + 32, pelX + 16, 2, width, height);
        split10_D2 = getRandomSplitForCU(pelY + 48, pelX     , 2, width, height);
        split11_D2 = getRandomSplitForCU(pelY + 48, pelX + 16, 2, width, height);

        str = [str ' ' split8_D2 ' ' split9_D2 ' ' split10_D2 ' ' split11_D2];
    end
    
    if (split3_D1 == '1')
        split12_D2  = getRandomSplitForCU(pelY + 32, pelX + 32, 2, width, height);
        split13_D2  = getRandomSplitForCU(pelY + 32, pelX + 48, 2, width, height);
        split14_D2  = getRandomSplitForCU(pelY + 48, pelX  +32, 2, width, height);
        split15_D2  = getRandomSplitForCU(pelY + 48, pelX + 48, 2, width, height);

        str = [str ' ' split12_D2 ' ' split13_D2 ' ' split14_D2 ' ' split15_D2];
    end
end


function split = getRandomSplitForCU(pelY, pelX, depth, width, height)

cuSize = 64 / (2^depth);

%Checks if this CU fits in the frame.
if ((pelY + cuSize < height) && (pelX + cuSize < width))
    split = char(round(rand()) + 48);
else
    split = '1';
end
