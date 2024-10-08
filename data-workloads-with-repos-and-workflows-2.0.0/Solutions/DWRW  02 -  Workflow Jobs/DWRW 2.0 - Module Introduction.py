# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
# MAGIC </div>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Orchestration with Databricks Workflow Jobs
# MAGIC This module is part of the Data Engineer Learning Path by Databricks Academy.
# MAGIC
# MAGIC #### Lessons
# MAGIC Lecture: Introduction to Workflows <br>
# MAGIC Lecture: Building and Monitoring Workflow Jobs <br>
# MAGIC DWRW 2.1 - Scheduling Tasks with the Jobs UI <br>
# MAGIC
# MAGIC &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DWRW 2.1.1 - Task Orchestration]($./DWRW 2.1 - Scheduling Tasks with the Jobs UI/DWRW 2.1.1 - Task Orchestration) <br>
# MAGIC &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DWRW 2.1.2 - Reset]($./DWRW 2.1 - Scheduling Tasks with the Jobs UI/DWRW 2.1.2 - Reset) <br>
# MAGIC &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DWRW 2.1.3 - DLT Job]($./DWRW 2.1 - Scheduling Tasks with the Jobs UI/DWRW 2.1.3 - DLT Job) <br>
# MAGIC
# MAGIC DWRW 2.2L - Jobs Lab <br>
# MAGIC
# MAGIC &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DWRW 2.2.1L - Lab Instructions]($./DWRW 2.2L - Jobs Lab/DWRW 2.2.1L - Lab Instructions) <br>
# MAGIC &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DWRW 2.2.2L - Batch Job]($./DWRW 2.2L - Jobs Lab/DWRW 2.2.2L - Batch Job) <br>
# MAGIC &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DWRW 2.2.3L - DLT Job]($./DWRW 2.2L - Jobs Lab/DWRW 2.2.3L - DLT Job) <br>
# MAGIC &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DWRW 2.2.4L - Exploring Results]($./DWRW 2.2L - Jobs Lab/DWRW 2.2.4L - Exploring Results) <br>
# MAGIC
# MAGIC #### Prerequisites
# MAGIC * Ability to perform basic code development tasks using Databricks (create clusters, run code in notebooks, use basic notebook operations, import repos from git, etc)
# MAGIC * Ability to configure and run data pipelines using the Delta Live Tables UI
# MAGIC * Beginner experience defining Delta Live Tables (DLT) pipelines using PySpark
# MAGIC   * Ingest and process data using Auto Loader and PySpark syntax
# MAGIC   * Process Change Data Capture feeds with APPLY CHANGES INTO syntax
# MAGIC * Review pipeline event logs and results to troubleshoot DLT syntax
# MAGIC * Production experience working with data warehouses and data lakes

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC &copy; 2024 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
# MAGIC <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
# MAGIC <a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
# MAGIC <a href="https://help.databricks.com/">Support</a>
