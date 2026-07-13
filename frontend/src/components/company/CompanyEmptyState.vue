<template>

<div class="empty-state text-center py-5">


    <i 
        :class="icon"
        class="empty-icon"
    ></i>



    <h5 class="mt-3">

        {{ title }}

    </h5>



    <p>

        {{ message }}

    </p>


</div>


</template>



<script setup>

defineProps({

    icon: {

        type:String,

        default:"bi bi-inbox"

    },


    title: {

        type:String,

        default:"No Data Found"

    },


    message: {

        type:String,

        default:"There is nothing to display here."

    }

})


</script>



<style scoped>

.empty-state{

    background:#F8FAFC;

    border-radius:16px;

    border:1px dashed #CBD5E1;

}



.empty-icon{

    font-size:45px;

    color:#94A3B8;

}



h5{

    color:#334155;

    font-weight:600;

}



p{

    color:#64748B;

    margin:0;

}



</style>