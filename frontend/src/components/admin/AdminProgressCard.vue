<script setup>

import { computed } from "vue"


const props = defineProps({

    title:{
        type:String,
        default:""
    },

    label:{
        type:String,
        default:""
    },

    value:{
        type:Number,
        default:0
    },

    total:{
        type:Number,
        default:0
    },

    color:{
        type:String,
        default:"primary"
    }

})


const percentage = computed(()=>{

    if(props.total <= 0)
        return 0

    return Math.round(
        (props.value / props.total) * 100
    )

})


</script>


<template>


<div class="card admin-card shadow-sm h-100">


<div class="card-body">


<div class="d-flex justify-content-between">


<h6>

{{title}}

</h6>


<strong>

{{percentage}}%

</strong>


</div>



<div class="progress mt-3">


<div

class="progress-bar"

:class="'bg-'+color"

:style="{
width:percentage+'%'
}"

>

</div>


</div>



<div class="mt-3 text-muted">


{{label}}

:

{{value}}

/

{{total}}


</div>


</div>


</div>


</template>