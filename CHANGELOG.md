# Version History

## 0.1.0.dev0

* Developer release (not public to pip)
* Update depends light-compressor==0.1.0.dev3
* Update depends nativelib==0.2.3.dev4
* Update depends pgcopylib==0.2.4.dev0
* Update depends pgpack==0.3.3.dev1
* Update README.md
* Add CompressionLevel to import
* Add optional compression_level parameter

## 0.0.2.5

* Update depends light-compressor==0.0.2.2
* Update depends nativelib==0.2.2.6
* Update depends pgcopylib==0.2.3.3
* Update depends pgpack==0.3.2.3
* Change documentation link
* Change project development status to 4 - Beta

## 0.0.2.4

* Update depends nativelib==0.2.2.5

## 0.0.2.3

* Update depends pgcopylib==0.2.3.2
* Update depends pgpack==0.3.2.2
* Fix build from source on unix systems

## 0.0.2.2

* Update depends pgcopylib==0.2.3.1
* Update depends pgpack==0.3.2.1

## 0.0.2.0

* Update depends pgcopylib==0.2.2.8
* Update depends pgpack==0.3.1.7

## 0.0.1.6

* Update depends light-compressor==0.0.2.1
* Update depends nativelib==0.2.2.4
* Update depends pgcopylib==0.2.2.7
* Update depends pgpack==0.3.1.6
* Back compile depends to cython>=0.29.33
* Make wheels for python 3.10-3.14

## 0.0.1.5

* Update depends light-compressor==0.0.2.0
* Update depends nativelib==0.2.2.3
* Update depends pgcopylib==0.2.2.6
* Update depends pgpack==0.3.1.5
* Downgrade compile depends to cython==0.29.33
* Make wheels for python 3.10 and 3.11 only

## 0.0.1.4

* Update depends nativelib==0.2.2.2

## 0.0.1.3

* Update depends pgcopylib==0.2.2.5
* Update depends pgpack==0.3.1.4
* Improve invalid byte sequence for encoding "UTF8": 0x00
* Disable Linux Aarch64

## 0.0.1.2

* Update depends pgcopylib==0.2.2.4
* Update depends pgpack==0.3.1.3

## 0.0.1.1

* Update depends pgcopylib==0.2.2.3
* Update depends pgpack==0.3.1.2

## 0.0.1.0

* Add dump_recovery(file_path, recovery_path) function
* Update depends light-compressor==0.0.1.9
* Update depends nativelib==0.2.2.1
* Update depends pgcopylib==0.2.2.2
* Update depends pgpack==0.3.1.1
* Update README.md

## 0.0.0.6

* Update depends nativelib==0.2.1.3
* Update depends pgcopylib==0.2.2.0
* Update depends pgpack==0.3.1.0

## 0.0.0.5

* Update depends light-compressor==0.0.1.8
* Update depends nativelib==0.2.1.2
* Update depends pgcopylib==0.2.1.9
* Update depends pgpack==0.3.0.9
* Update python version support to 3.10-3.14
* Add auto upload to pip

## 0.0.0.4

* Update depends nativelib==0.2.1.1
* Update depends pgcopylib==0.2.1.8
* Update depends pgpack==0.3.0.8

## 0.0.0.3

* Add wheels automake
* Change nativelib cimport to import

## 0.0.0.2

* Fix initialize compression_method from string
* Fix convert from native dump to pgpack/pgcopy

## 0.0.0.1

First version of the library dbhose_utils
