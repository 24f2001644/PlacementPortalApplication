<script setup>

import {
    Bar
} from "vue-chartjs"

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

    labels:{
        type:Array,
        default:()=>[]
    },

    values:{
        type:Array,
        default:()=>[]
    }

})


const data = {

    labels: props.labels,

    datasets:[

        {

            label:"Students",

            data:props.values

        }

    ]

}



const options={

    responsive:true,

    maintainAspectRatio:false,

    plugins:{

        legend:{
            display:true
        }

    }

}


</script>


<template>

<div style="height:320px">

    <Bar

        :data="data"

        :options="options"

    />

</div>


</template>