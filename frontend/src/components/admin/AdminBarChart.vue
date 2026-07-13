<script setup>

import {

Bar

}

from "vue-chartjs"

import {

Chart as ChartJS,

CategoryScale,

LinearScale,

BarElement,

Tooltip,

Legend

}

from "chart.js"

ChartJS.register(

CategoryScale,

LinearScale,

BarElement,

Tooltip,

Legend

)

const props = defineProps({

labels:Array,

values:Array

})

const data={

labels:props.labels,

datasets:[

{

label:"Students",

data:props.values,

backgroundColor:"#6366f1"

}

]

}

const options={

responsive:true,

maintainAspectRatio:false

}

</script>

<template>

<div class="card admin-card">

<div class="card-header">

Branch Wise Students

</div>

<div

style="height:320px"

class="p-3"

>

<Bar

:data="data"

:options="options"

/>

</div>

</div>

</template>