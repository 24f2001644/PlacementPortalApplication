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

<style scoped>


.section-card{


    background:white;

    border-radius:18px;

    box-shadow:0 8px 24px rgba(0,0,0,.05);

    overflow:hidden;

    margin-bottom:25px;


}



.section-header{


    padding:18px 25px;

    border-bottom:1px solid #E2E8F0;

    background:#F8FAFC;


}



.section-header h5{


    margin:0;

    font-size:18px;

    font-weight:700;

    color:#0F172A;


}



.section-body{


    padding:25px;


}




@media(max-width:768px){


    .section-body{


        padding:18px;


    }



    .section-header{


        padding:15px 18px;


    }


}


</style>