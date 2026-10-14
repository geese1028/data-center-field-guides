#!/usr/bin/env python3
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = "/Users/geese/Library/CloudStorage/OneDrive-Personal"
LIST = "/tmp/od_missing.txt"
LOG = "/Users/geese/Downloads/book/sources/hydrate.log"
OK = "/Users/geese/Downloads/book/sources/hydrate_ok.txt"
SF_DATALESS = 0x40000000
WORKERS = 4


def hydrate(rel):
    full = os.path.join(ROOT, rel)
    if not os.path.lexists(full):
        return rel, "missing"
    try:
        flags = getattr(os.lstat(full), "st_flags", 0)
        if not (flags & SF_DATALESS):
            return rel, "already"
        with open(full, "rb") as handle:
            while handle.read(1024 * 1024):
                pass
        flags = getattr(os.lstat(full), "st_flags", 0)
        if flags & SF_DATALESS:
            return rel, "still_dataless"
        if os.path.getsize(full) <= 0:
            return rel, "empty"
        return rel, "ok"
    except Exception as exc:
        return rel, f"error:{type(exc).__name__}"


def main():
    paths = [line.rstrip("\n") for line in open(LIST, encoding="utf-8") if line.strip()]
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    counts = {}
    done = 0
    with open(LOG, "w", encoding="utf-8") as log, open(OK, "w", encoding="utf-8") as ok:
        log.write(f"total {len(paths)}\n")
        log.flush()
        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futures = [pool.submit(hydrate, rel) for rel in paths]
            for fut in as_completed(futures):
                rel, status = fut.result()
                counts[status] = counts.get(status, 0) + 1
                done += 1
                if status in ("ok", "already"):
                    ok.write(rel + "\n")
                    ok.flush()
                if status not in ("ok", "already") or done % 50 == 0:
                    log.write(f"{done}\t{status}\t{rel}\n")
                    log.flush()
        log.write("COUNTS " + " ".join(f"{k}={v}" for k, v in sorted(counts.items())) + "\n")
    print("COUNTS", counts)


if __name__ == "__main__":
    sys.exit(main() or 0)
