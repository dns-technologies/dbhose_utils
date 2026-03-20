from light_compressor import (
    CompressionLevel,
    CompressionMethod,
)


LEVEL = {
    CompressionMethod.GZIP: CompressionLevel.GZIP_DEFAULT,
    CompressionMethod.LZ4: CompressionLevel.LZ4_DEFAULT,
    CompressionMethod.NONE: CompressionLevel.NO_COMPRESSION,
    CompressionMethod.SNAPPY: CompressionLevel.SNAPPY_DEFAULT,
    CompressionMethod.ZSTD: CompressionLevel.ZSTD_DEFAULT,
}
