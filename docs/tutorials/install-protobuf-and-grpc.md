# Install Protobuf and gRPC on Ubuntu using CMake

## Pre-requisites
Clone [https://github.com/grpc/grpc](https://github.com/grpc/grpc) and follow the instructions:

```bash
sudo apt-get install build-essential autoconf libtool pkg-config
sudo apt-get install cmake

git clone https://github.com/grpc/grpc
cd grpc
git submodule update --init
```

## Install Protobuf
Go to the submodule:
```bash
cd third_party/protobuf
```

Follow instructions from [https://github.com/protocolbuffers/protobuf](https://github.com/protocolbuffers/protobuf)
```bash
sudo apt-get install autoconf automake libtool curl make g++ unzip
git submodule update --init --recursive
./autogen.sh
./configure
make
make check
sudo make install
sudo ldconfig 
```

## Install gRPC Dependencies
Script `test/distrib/cpp/run_distrib_test_cmake.sh` can be used:
```bash
./test/distrib/cpp/run_distrib_test_cmake.sh
```

For me the command above failed.

## Manual Installation
```bash
cmake -DgRPC_INSTALL=ON -DgRPC_BUILD_TESTS=OFF -DgRPC_PROTOBUF_PROVIDER=package -DgRPC_ZLIB_PROVIDER=package -DgRPC_CARES_PROVIDER=package -DgRPC_SSL_PROVIDER=package -DCMAKE_BUILD_TYPE=Release ../..

cmake --build . -j 4 -v

sudo make install
sudo ldconfig
```

## Missing Dependency
Dependency for `abseil-cpp` was missing:
```
mkdir build
cd build
cmake -DABSL_USE_GOOGLETEST_HEAD=ON -DABSL_RUN_TESTS=ON ..

make -j4

sudo make install
sudo ldconfig
```