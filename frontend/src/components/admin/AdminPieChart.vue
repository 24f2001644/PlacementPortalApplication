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



const props = defineProps({

    labels:{
        type:Array,
        default:()=>[]
    },

    values:{
        type:Array,
        default:()=>[]
    }

})



const data={


labels:props.labels,


datasets:[

{

data:props.values

}

]


}



const options={

responsive:true,

maintainAspectRatio:false


}


</script>


<template>


<div style="height:320px">


<Pie

:data="data"

:options="options"

/>


</div>


</template>