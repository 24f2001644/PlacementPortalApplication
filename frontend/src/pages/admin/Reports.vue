<template>

<div class="container mt-4">

<div class="card shadow">

<div class="card-header bg-success text-white">

<h3>Placement Reports</h3>

</div>

<div class="card-body">

<table class="table table-bordered">

<thead>

<tr>

<th>Metric</th>

<th>Value</th>

</tr>

</thead>

<tbody>

<tr>

<td>Total Students</td>

<td>{{ report.students }}</td>

</tr>

<tr>

<td>Total Companies</td>

<td>{{ report.companies }}</td>

</tr>

<tr>

<td>Total Drives</td>

<td>{{ report.drives }}</td>

</tr>

<tr>

<td>Total Applications</td>

<td>{{ report.applications }}</td>

</tr>

<tr>

<td>Selected Students</td>

<td>{{ report.selected }}</td>

</tr>

<tr>

<td>Placement Percentage</td>

<td>{{ report.percentage }}%</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</template>

<script setup>

const report={

students:240,

companies:36,

drives:18,

applications:520,

selected:130,

percentage:54

}

</script>