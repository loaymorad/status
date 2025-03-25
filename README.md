# status
it is for bugbounty hunter and penetration testers to know status code of urls after recon and find alot of subdomains

## How to use
**Simple command**
```sh
python status.py -f filehasdomains.txt -o outputfile.txt
```
`-f` file that has the urls want to test status
`-o` output file

**Advanced commands**
```sh
python status.py -f filehasdomains.txt -o outputfile.txt -so200 file
```
```sh
python status.py -f filehasdomains.txt -o outputfile.txt -so200,400 file
```
`-so` for status output will get all 200 domains and put it in file_200.txt the same for 400, can add more status code as you like

```sh
python status.py -f filehasdomains.txt -o outputfile.txt -sa file
```
`-sa` for status automated do same thing as `-so` but automated no need to specify status codes 

## Tool cost
صلى على سيدنا محمد
