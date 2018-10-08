Here's my solution for today's homework exercise.

---

The first one-liner takes `tableofSNPs.csv` and does the following:

1. Matches all strings of double-quotes + (either 1-3 digits + comma, or empty) + 1-3
   digits + comma + 3 digits + double-quotes
2. While doing so, captures the constituent strings of 1-3 digits
3. Replaces the matched string with just the two or three captured strings, in order,
   with no delimiters
4. Saves the results to `tableofSNPsCorrected.csv`

```
gsed -E 's/\"([0-9]{0,3})\,?([0-9]{1,3})\,([0-9]{3})\"/\1\2\3/g' tableofSNPs.csv > tableofSNPsCorrected.csv
```

---

The second one-liner returns only the lines of `tableofSNPsCorrected.csv` that do not
consist of strings of non-comma characters separated by exactly three commas. If it 
returns anything at all, the first one-liner didn't work correctly.

```
ggrep '^[^,]*\,[^,]*\,[^,]*\,[^,]*$' -v  tableofSNPsCorrected.csv
```

---

The third one-liner reverses all A and T nucleotides. It consists of three `sed` commands:

* The first replaces all "A"s with "µ"s, to keep nucleotides permuted as A from being
  mixed up with the Ts about to be re-permuted _back_ to A. (Lowercase mu is just an 
  easy-to-type character that doesn't appear elsewhere in the data file.)
* The second replaces all "T"s with "A"s.
* The third replaces all "µ"s with "T"s.

```
sed 's/A/µ/g' tableofSNPsCorrected.csv | sed 's/T/A/g' | sed 's/µ/T/g' > tableofSNPsRepermuted.csv
```

---

The last few lines of code check whether the third one-liner worked correctly.

This one checks whether there are any mus remaining in the text. If there are, the third
one-liner didn't work correctly.

```
grep "µ" tableofSNPsRepermuted.csv
```

Of these three, the first two get a list of unique SNP names and counts from the original 
data and the permuted data, sort each list numerically, remove all SNPs that have neither 
A nor T, strip out excess spaces at the beginnings of lines, and save each list as a text 
file. The third line pastes the two lists side-by-side, for easy comparison.

If the numbers in columns 1 and 3 of the last line's output differ for any row, the third 
one-liner (above) didn't work correctly. Conveniently, this also lines up the re-permuted 
SNPs for a triple-check by eyeballing.

```
gsed -E 's/^([ACGT]*),.*/\1/g' tableofSNPsCorrected.csv | sort | uniq -c | sort | grep '[TA]' | sed 's/  / /g' | gsed 's/^ //g' > SNPListCorrected.txt
gsed -E 's/^([ACGT]*),.*/\1/g' tableofSNPsRepermuted.csv | sort | uniq -c | sort | grep '[TA]' | sed 's/  / /g' | gsed 's/^ //g' > SNPListRepermuted.txt
paste SNPListCorrected.txt SNPListRepermuted.txt
```

