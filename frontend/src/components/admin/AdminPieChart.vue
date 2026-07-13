<script setup>

import {

Pie

}

from "vue-chartjs"

import {

Chart as ChartJS,

ArcElement,

Tooltip,

Legend

}

from "chart.js"

ChartJS.register(

ArcElement,

Tooltip,

Legend

)

const props=defineProps({

labels:Array,

values:Array

})

const data={

labels:props.labels,

datasets:[

{

data:props.values,

backgroundColor:[

"#6366f1",

"#22c55e",

"#f59e0b",

"#ef4444"

]

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

Applications

</div>

<div

style="height:320px"

class="p-3"

>

<Pie

:data="data"

:options="options"

/>

</div>

</div>

</template>