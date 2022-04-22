# My 'Adventofcode'
- Create dirs structure
```sh
_yy_=2015; for i in $(seq 1 25); do mkdir -p aoc$_yy_/day${(l:2::0:)i}; done 
```
- Download problems
```sh
_yy_=2015; for i in $(seq 1 25); do w3m -dump https://adventofcode.com/$_yy_/day/${i} >aoc$_yy_/day${(l:2::0:)i}/p1.txt; done
```
- Parse problems
```sh
_yy_=2015; for i in $(seq 1 25); do _ff_=aoc$_yy_/day${(l:2::0:)i}/p1.txt; _ll_=$(wc -l $_ff_ | cut -d ' ' -f 1); head -$(expr $_ll_ - 4) $_ff_ | tail -$(expr $_ll_ - 18) >$_ff_.new; done
```
- Download inputs
> **Needed** session cookie
```sh
_yy_=2015; for i in $(seq 1 25); do curl https://adventofcode.com/$_yy_/day/${i}/input -X GET -H 'Cookie:session=53...f1' -o aoc$_yy_/day${(l:2::0:)i}/input.txt; done
```
- Copy template
```sh
_yy=2015; for i in $(seq 1 25); do cp template.py aoc$_yy/day${(l:2::0:)i}/s1.py; cp template.py aoc$_yy/day${(l:2::0:)i}/s2.py; done
```
