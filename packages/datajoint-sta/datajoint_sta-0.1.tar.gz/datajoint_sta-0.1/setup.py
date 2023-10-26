from distutils.core import setup
setup(
  name = 'datajoint_sta',         
  packages = ['datajoint_sta'],   
  version = '0.1',      
  license='MIT',       
  description = 'calculating spike trigerred average',   
  author = 'Aghil Zadeh',                   
  author_email = 'agheal@gmail.com',    
  url = 'https://github.com/AghilZadeh/datajoint_sta',   
  download_url = 'https://github.com/AghilZadeh/datajoint_sta/archive/v_01.tar.gz',    
  keywords = ['spike', 'neural activity', 'datajoint'],  
  install_requires=[           
          'matplotlib',
          'pickle',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
