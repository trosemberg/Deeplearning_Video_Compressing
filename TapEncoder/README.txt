Para rodar o HEVC

O arquivo de video tem essa nomenclatura:
Crowdrun_1920x1080_50_8bit_420
<nome> _ <WIDTH> x <HEIGHT> _ <FRAME_RATE> _ <BITDEPTH> _ <FORMATO>

TAppEncoder -c encoder_randomaccess_main.cfg

Parametros para mudar no config file (.cfg):
 InputFile -> O arquivo de vídeo de entrada.
 FrameRate -> Deve ser o mesmo que o arquivo.
 FramesToBeEncoded ->
 
 QP   -> Deve ser 37, 32, 27 ou 22. 
 
 TAppEncoder -c encoder_randomaccess_main.cfg -q 37
 TAppEncoder -c encoder_randomaccess_main.cfg -q 32
 TAppEncoder -c encoder_randomaccess_main.cfg -q 27
 TAppEncoder -c encoder_randomaccess_main.cfg -q 22
 
  -i <input_file>
  -fr <frame_rate>
  -f <numero_de_frames_para_codificar>