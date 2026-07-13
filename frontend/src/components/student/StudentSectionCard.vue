<template>


<div class="section-card">


    <!-- Header -->


    <div class="section-header" v-if="title">


        <h5>

            {{ title }}

        </h5>


    </div>



    <!-- Content -->


    <div class="section-body">


        <slot></slot>


    </div>



</div>


</template>



<script setup>


defineProps({


    title:{


        type:String,

        default:""


    }


})


</script>

part2