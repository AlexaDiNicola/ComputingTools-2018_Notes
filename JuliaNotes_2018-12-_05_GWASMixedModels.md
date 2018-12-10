# Julia for GWAS and Mixed Models

[Dr. Doug Bates](https://github.com/dmbates), of NLME and various mixed-model packages. Wrote a lot of Julia, too.

* The tools we have are "an embarrassment of riches" given that he started in the days of S and FORTRAN. He seems delighted about it.
* Bell Labs back in the day: techie fraternity, rivalry with the Bell lawyers/accountants. Somebody discovered that you couldn't copyright a single-letter name -- hence R, C, B, and S. They just wanted to annoy the bean counters.
  * "R" was "not unlike S", but developed by a Ross and a Robert, so they stepped back a letter to R
  * Julia named for "no particular reason at all." Logo actually developed before the name.

##Dealing with "big data" in Julia

- Exactly what "big data" is evolves over time.

    - DB's blog called "A Second Megabyte of Memory" because he'd spent an extravagant $8k for *2* MB memory in the department's first computer...
    - He'll discuss one instance of modern big data

- current constraints can be
    - many observations on a relatively simple structure
    - complex models fit to moderately large data sets
    - iterative methods with vague stopping rules
        - MCMC (Markov Chain Monte Carlo)
        - many machine-learning approaches
### [GWAS](https://en.wikipedia.org/wiki/Genome-wide_association_study) (Genome-Wide Association Studies)

* GWAS data:
	- two allele types at `n` SNP (single-nucleotide polymorphism) sites
    - `m` individuals
    - [Recent arrays](https://en.wikipedia.org/wiki/SNP_genotyping) allow for $n > 10^6$
    - Some studies also have $m\approx 10^6$ or $> 10^{12}$ obs.

- Here's an example from a European dataset.

    - Columns: chromosome, SNP name, (allele frequency?), nucleotide position, major allele (M), minor allele (m).
    - 3 possiblities (mm, mM, MM) or missing data at each position (so 4 possibilities)

- Often stored as a [PLINK binary biallelic genetype table](https://www.cog-genomics.org/plink2/formats#bed) (pronounced "P-link"), `.bed` file
    - each observation as 2 bits, i.e. 4 obs. per byte
    - column-major order - obs. on same SNP are adjacent
    - columns are padded to a full byte
    - two "magic numbers" at the start of the file. (A signature to indicate file type?)
    - even this compacted format can be terabytes in size


- Initial analysis can be just a summary - mean, variance, minor-allele frequency. Build out the table as you go, building models and such.


- Later may want to construct (empirical) "genetic relationship matrix", data on who's related to who among your subjects *inferred from genotype similarity*

### Handling really big PLINKs


- For small studies, you can read in the data as some type of integer or float and work with those. Won't work for large studies, when you need 32 or 64 bits (not just 2!) per individual...
- May be able to stream the data, but you don't want to do many passes in that case.

    - (This was actually a major advantage of R: earlier langs assumed your data was on read-only tape, so they streamed *everything.*)
    - And there's always an inherent roadblock in tracking a stream: reading data is a fairly "expensive" operation, with a lot of computational overhead.
- [Memory-mapped files](https://en.wikipedia.org/wiki/Memory-mapped_file) provide an alternative

    - Takes contents of a file, pinpoints their starting address, and has addresses flow on from there.
    - Can also allow for parallel processing -- split the SNPs into disjoint sets and assign among machines
    - Substantial advantage when using a read-only data file and writing to a different one.

###[A Julia package for GWAS parsing](https://github.com/dmbates/BEDFiles.jl)


```julia
using Pkg
Pkg.add(PackageSpec(url="https://github.com/dmbates/BEDFiles.jl", rev="staticslices"))
```
* Converts a PLINK/.bed into memory-mapped version?
* *Aside: Confounding pointers with offsets, thus zero-indexing, was one of C's "original sins." It's now the single biggest source of bugs and security holes.*
* Can also generate empirical relationship matrices from SNP data (different script?)
* In Julia, to keep things fast, you want to avoid making copies. Thus the common construction of feeding in both the input and output vectors -- e.g. `function uvals!(uv::Vector{<:AbstractFloat}, v::AbstractVector{<:Integer})`
* Basically, in Visual Studio Code, you can work in Julia as if in R or Python. Can do some "spontaneous exploring" to decide on best language for any given step of any given problem.

## Mixed-effects models

* DB got into this for modeling stuff like lactation curves, where there's variability between animals but structural similarity
* Nested structure of models: one level for random effects, lower levels associated with only 1 value on the next level up
* This is what went into NLME (NonLinear Mixed-Effects models).
* RData package lets Julia read `.rda`

