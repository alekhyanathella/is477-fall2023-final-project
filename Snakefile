rule prepare:
  output:
    "data/iris/iris.data"
  shell:
    "python scripts/prepare_data.py"

rule profile:
  input:
    "data/iris/iris.data"
  output:
    "profiling/report.html"
  shell:
    "python scripts/profile.py"

rule analyze:
  input:
    "data/iris/iris.data"
  output:
    "results/bar-plot.jpg",
    "results/summary.txt"
  shell:
    "python scripts/analysis.py"

rule reproduce:
  input:
    "results/bar-plot.jpg",
    "results/summary.txt",
    "profiling/report.html"

