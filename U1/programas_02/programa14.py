bytes = int(input("Introduce el número de bytes: "))

gb_si = bytes // 1_000_000_000
mb_si = (bytes % 1_000_000_000) // 1_000_000
kb_si = (bytes % 1_000_000) // 1_000
b_si = bytes % 1_000
print(
    bytes,
    "bytes en sistema decimal (SI):",
    gb_si,
    "GB,",
    mb_si,
    "MB,",
    kb_si,
    "KB,",
    b_si,
    "bytes",
)

gb_iec = bytes // 1_073_741_824
mb_iec = (bytes % 1_073_741_824) // 1_048_576
kb_iec = (bytes % 1_048_576) // 1_024
b_iec = bytes % 1_024
print(
    bytes,
    "bytes en sistema binario (IEC):",
    gb_iec,
    "GiB,",
    mb_iec,
    "MiB,",
    kb_iec,
    "KiB,",
    b_iec,
    "bytes",
)
