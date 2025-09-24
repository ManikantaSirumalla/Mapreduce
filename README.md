# Harry Potter MapReduce (DOB: 28-Oct-1999)

Single-node Hadoop Streaming jobs on macOS (Apple Silicon, Hadoop 3.4.2, Java 17) to:
1) Word count on selected pages (`file1.txt`)
2) Non-English token count on selected pages (`file2.txt`)

## Environment
- Hadoop: 3.4.2 lean at `~/MS-hadoop-3.4.2/MS-hadoop`
- Java: JDK 17
- HDFS: hdfs://localhost:9000

## Local Layout
- `file1.txt`, `file2.txt`
- `mapper_wordcount.py`, `mapper_nonenglish.py`, `reducer_sum.py`
- `words.txt`
- `outputs/wordcount_sorted.txt`, `outputs/nonenglish_sorted.txt`
