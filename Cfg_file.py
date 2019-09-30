import re
class cfg:
    def __init__(self):
        self.config = """
        #======== File I/O ===============
InputFile                     : ../Videos/{Video}
InputBitDepth                 : 8           # Input bitdepth
InputChromaFormat             : 420         # Ratio of luminance to chrominance samples
FrameRate                     : {fps}          # Frame Rate per second
FrameSkip                     : {start}           # Number of frames to be skipped in input
SourceWidth                   : {width}        # Input  frame width
SourceHeight                  : {height}        # Input  frame height
FramesToBeEncoded             : {frames}           # Number of frames to be coded

Level                         : 4.1

#======== File I/O =====================
BitstreamFile                 : str.bin
ReconFile                     : rec.yuv

#======== Profile ================
Profile                       : main

#======== Unit definition ================
MaxCUWidth                    : 64          # Maximum coding unit width in pixel
MaxCUHeight                   : 64          # Maximum coding unit height in pixel
MaxPartitionDepth             : 4           # Maximum coding unit depth
QuadtreeTULog2MaxSize         : 5           # Log2 of maximum transform size for
                                            # quadtree-based TU coding (2...6)
QuadtreeTULog2MinSize         : 2           # Log2 of minimum transform size for
                                            # quadtree-based TU coding (2...6)
QuadtreeTUMaxDepthInter       : 3
QuadtreeTUMaxDepthIntra       : 3

#======== Coding Structure =============
IntraPeriod                   : 32          # Period of I-Frame ( -1 = only first)
DecodingRefreshType           : 1           # Random Accesss 0:none, 1:CRA, 2:IDR, 3:Recovery Point SEI
GOPSize                       : 16           # GOP Size (number of B slice = GOPSize-1)
ReWriteParamSetsFlag          : 1           # Write parameter sets with every IRAP

IntraQPOffset                 : -3
LambdaFromQpEnable            : 1           # see JCTVC-X0038 for suitable parameters for IntraQPOffset, QPoffset, QPOffsetModelOff, QPOffsetModelScale when enabled
#        Type POC QPoffset QPOffsetModelOff QPOffsetModelScale CbQPoffset CrQPoffset QPfactor tcOffsetDiv2 betaOffsetDiv2 temporal_id #ref_pics_active #ref_pics reference pictures     predict deltaRPS #ref_idcs reference idcs
Frame1:  B   16   1        0.0                      0.0            0          0          1.0      0            0              0           2                3         -16 -24 -32            0  
Frame2:  B    8   1       -4.8848                   0.2061         0          0          1.0      0            0              1           2                3         -8  -16   8            1       8        4         1 1 0 1    
Frame3:  B    4   4       -5.7476                   0.2286         0          0          1.0      0            0              2           2                4         -4  -12   4  12        1       4        4         1 1 1 1 
Frame4:  B    2   5       -5.90                     0.2333         0          0          1.0      0            0              3           2                5         -2  -10   2   6  14    1       2        5         1 1 1 1 1 
Frame5:  B    1   6       -7.1444                   0.3            0          0          1.0      0            0              4           2                5         -1    1  3    7  15    1       1        6         1 0 1 1 1 1  
Frame6:  B    3   6       -7.1444                   0.3            0          0          1.0      0            0              4           2                5         -1   -3   1   5  13    1      -2        6         1 1 1 1 1 0 
Frame7:  B    6   5       -5.90                     0.2333         0          0          1.0      0            0              3           2                4         -2   -6   2  10        1      -3        6         0 1 1 1 1 0 
Frame8:  B    5   6       -7.1444                   0.3            0          0          1.0      0            0              4           2                5         -1   -5   1   3  11    1       1        5         1 1 1 1 1  
Frame9:  B    7   6       -7.1444                   0.3            0          0          1.0      0            0              4           2                5         -1   -3  -7   1   9    1      -2        6         1 1 1 1 1 0 
Frame10: B   12   4       -5.7476                   0.2286         0          0          1.0      0            0              2           2                3         -4  -12   4            1      -5        6         0 0 1 1 1 0 
Frame11: B   10   5       -5.90                     0.2333         0          0          1.0      0            0              3           2                4         -2  -10   2   6        1       2        4         1 1 1 1 
Frame12: B    9   6       -7.1444                   0.3            0          0          1.0      0            0              4           2                5         -1   -9   1   3   7    1       1        5         1 1 1 1 1 
Frame13: B   11   6       -7.1444                   0.3            0          0          1.0      0            0              4           2                5         -1   -3 -11   1   5    1      -2        6         1 1 1 1 1 0 
Frame14: B   14   5       -5.90                     0.2333         0          0          1.0      0            0              3           2                4         -2   -6 -14   2        1      -3        6         0 1 1 1 1 0 
Frame15: B   13   6       -7.1444                   0.3            0          0          1.0      0            0              4           2                5         -1   -5 -13   1   3    1       1        5         1 1 1 1 1 
Frame16: B   15   6       -7.1444                   0.3            0          0          1.0      0            0              4           2                5         -1   -3 -7  -15   1    1      -2        6         1 1 1 1 1 0 

#=========== Motion Search =============
FastSearch                    : 1           # 0:Full search  1:TZ search
SearchRange                   : 384         # (0: Search range is a Full frame)
ASR                           : 1           # Adaptive motion search range
MinSearchWindow               : 96          # Minimum motion search window size for the adaptive window ME
BipredSearchRange             : 4           # Search range for bi-prediction refinement
HadamardME                    : 1           # Use of hadamard measure for fractional ME
FEN                           : 1           # Fast encoder decision
FDM                           : 1           # Fast Decision for Merge RD cost

#======== Quantization =============
QP                            : {QP}          # Quantization parameter(0-51)
MaxDeltaQP                    : 0           # CU-based multi-QP optimization
MaxCuDQPDepth                 : 0           # Max depth of a minimum CuDQP for sub-LCU-level delta QP
DeltaQpRD                     : 0           # Slice-based multi-QP optimization
RDOQ                          : 1           # RDOQ
RDOQTS                        : 1           # RDOQ for transform skip
SliceChromaQPOffsetPeriodicity: 0           # Used in conjunction with Slice Cb/Cr QpOffsetIntraOrPeriodic. Use 0 (default) to disable periodic nature.
SliceCbQpOffsetIntraOrPeriodic: 0           # Chroma Cb QP Offset at slice level for I slice or for periodic inter slices as defined by SliceChromaQPOffsetPeriodicity. Replaces offset in the GOP table.
SliceCrQpOffsetIntraOrPeriodic: 0           # Chroma Cr QP Offset at slice level for I slice or for periodic inter slices as defined by SliceChromaQPOffsetPeriodicity. Replaces offset in the GOP table.

#=========== Deblock Filter ============
LoopFilterOffsetInPPS         : 1           # Dbl params: 0=varying params in SliceHeader, param = base_param + GOP_offset_param; 1 (default) =constant params in PPS, param = base_param)
LoopFilterDisable             : 0           # Disable deblocking filter (0=Filter, 1=No Filter)
LoopFilterBetaOffset_div2     : 0           # base_param: -6 ~ 6
LoopFilterTcOffset_div2       : 0           # base_param: -6 ~ 6
DeblockingFilterMetric        : 0           # blockiness metric (automatically configures deblocking parameters in bitstream). Applies slice-level loop filter offsets (LoopFilterOffsetInPPS and LoopFilterDisable must be 0)

#=========== Misc. ============
InternalBitDepth              : 8           # codec operating bit-depth

#=========== Coding Tools =================
SAO                           : 1           # Sample adaptive offset  (0: OFF, 1: ON)
AMP                           : 1           # Asymmetric motion partitions (0: OFF, 1: ON)
TransformSkip                 : 1           # Transform skipping (0: OFF, 1: ON)
TransformSkipFast             : 1           # Fast Transform skipping (0: OFF, 1: ON)
SAOLcuBoundary                : 0           # SAOLcuBoundary using non-deblocked pixels (0: OFF, 1: ON)

#============ Slices ================
SliceMode                : 0                # 0: Disable all slice options.
                                            # 1: Enforce maximum number of LCU in an slice,
                                            # 2: Enforce maximum number of bytes in an 'slice'
                                            # 3: Enforce maximum number of tiles in a slice
SliceArgument            : 1500             # Argument for 'SliceMode'.
                                            # If SliceMode==1 it represents max. SliceGranularity-sized blocks per slice.
                                            # If SliceMode==2 it represents max. bytes per slice.
                                            # If SliceMode==3 it represents max. tiles per slice.

LFCrossSliceBoundaryFlag : 1                # In-loop filtering, including ALF and DB, is across or not across slice boundary.
                                            # 0:not across, 1: across

#============ PCM ================
PCMEnabledFlag                      : 0                # 0: No PCM mode
PCMLog2MaxSize                      : 5                # Log2 of maximum PCM block size.
PCMLog2MinSize                      : 3                # Log2 of minimum PCM block size.
PCMInputBitDepthFlag                : 1                # 0: PCM bit-depth is internal bit-depth. 1: PCM bit-depth is input bit-depth.
PCMFilterDisableFlag                : 0                # 0: Enable loop filtering on I_PCM samples. 1: Disable loop filtering on I_PCM samples.

#============ Tiles ================
TileUniformSpacing                  : 0                # 0: the column boundaries are indicated by TileColumnWidth array, the row boundaries are indicated by TileRowHeight array
                                                       # 1: the column and row boundaries are distributed uniformly
NumTileColumnsMinus1                : 0                # Number of tile columns in a picture minus 1
TileColumnWidthArray                : 2 3              # Array containing tile column width values in units of CTU (from left to right in picture)   
NumTileRowsMinus1                   : 0                # Number of tile rows in a picture minus 1
TileRowHeightArray                  : 2                # Array containing tile row height values in units of CTU (from top to bottom in picture)

LFCrossTileBoundaryFlag             : 1                # In-loop filtering is across or not across tile boundary.
                                                       # 0:not across, 1: across 

#============ WaveFront ================
WaveFrontSynchro                    : 0                # 0:  No WaveFront synchronisation (WaveFrontSubstreams must be 1 in this case).
                                                       # >0: WaveFront synchronises with the LCU above and to the right by this many LCUs.

#=========== Quantization Matrix =================
ScalingList                   : 0                      # ScalingList 0 : off, 1 : default, 2 : file read
ScalingListFile               : scaling_list.txt       # Scaling List file name. If file is not exist, use Default Matrix.

#============ Lossless ================
TransquantBypassEnableFlag : 0                         # Value of PPS flag.
CUTransquantBypassFlagForce: 0                         # Force transquant bypass mode, when transquant_bypass_enable_flag is enabled

#============ Rate Control ======================
RateControl                         : 0                # Rate control: enable rate control
TargetBitrate                       : 1000000          # Rate control: target bitrate, in bps
KeepHierarchicalBit                 : 2                # Rate control: 0: equal bit allocation; 1: fixed ratio bit allocation; 2: adaptive ratio bit allocation
LCULevelRateControl                 : 1                # Rate control: 1: LCU level RC; 0: picture level RC
RCLCUSeparateModel                  : 1                # Rate control: use LCU level separate R-lambda model
InitialQP                           : 0                # Rate control: initial QP
RCForceIntraQP                      : 0                # Rate control: force intra QP to be equal to initial QP

#============ Deep Learning Fast Mode Decision ======================
WriteSplitDecision                  : {writesplit}
ByPassSplitDecision                 : {bypass}
m_bypassSplitDecision_Depth0        : {depth0}
m_bypassSplitDecision_Depth1        : {depth1}
m_bypassSplitDecision_Depth2        : {depth2}

### DO NOT ADD ANYTHING BELOW THIS LINE ###
### DO NOT DELETE THE EMPTY LINE BELOW ###
        """

    def choose_config(self,Video="Crowdrun_1920x1080_50_8bit_420.yuv",writesplit = 0,bypass=1,depth0=1,depth1=1,depth2=1,QP= 22,
                    start = 0, frames = 10):
        self.Video = Video
        self.QP = QP
        self.writesplit = writesplit
        self.bypass = bypass
        self.depth0 = depth0
        self.depth1 = depth1
        self.depth2 = depth2
        self.start = start
        self.frames = frames
        results = re.match(r"\w*_(\d*)x(\d*)_(\d*)_\w*_\d*.yuv",self.Video)
        self.width = results.group(1)
        self.height = results.group(2)
        self.fps = results.group(3)
        self.config_2 = self.config
        self.config_2 = self.config_2.format(Video = self.Video,writesplit = self.writesplit,bypass = self.bypass,
                                            depth0 = self.depth0,depth1 = self.depth1,depth2= self.depth2, width = self.width,
                                            QP = self.QP,fps = self.fps, start = self.start,
                                            height = self.height, frames = self.frames)

    def writefile(self):
        with open("./TapEncoder/encoder_randomaccess_main.cfg","w") as file:
            file.write(self.config_2)