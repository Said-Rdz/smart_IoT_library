# Smart IoT Library
import requests
import torchaudio 

def version():
  '''
    Shows smart IoT library version
  '''
  print('Smart IoT Library ver. 1.2.0')
  
def load_audio(url, fname):
  '''
  Regresa la señal de audio, sample-rate, metadata, byte-size
  '''
  r = requests.get(url)
  with open(fname, 'wb') as f:
    f.write(r.content)

  sz = len(r.content)
  meta = torchaudio.info(fname)
  wave, sr = torchaudio.load(fname)

  return (wave, sr, meta, sz)

def print_info(info, fname=None):
  if fname:
    print('-'*30)
    print('Filename: '+fname)
    print('-'*30)

  wave, sr, meta, sz= info
  channels, frames = wave.shape
  print(f'            Frames: {frames}')
  print(f'          Channels: {channels}')
  print(f'   Audio File Size: {sz} bytes')
  print(f'Tensor memory size: {wave.element_size() * channels * frames} bytes')
  print(f'             Dtype: {wave.dtype}')
  print(f'               Max: {wave.max().item():6.3f}')
  print(f'               Min: {wave.min().item():6.3f}')
  print(f'              Mean: {wave.mean().item():6.3f}')
  print(f'           Std Dev: {wave.max().std():6.3f}')
  print(wave)
