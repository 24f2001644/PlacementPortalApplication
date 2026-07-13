<template>


<div class="loading-container">


    <div class="spinner-border text-primary" role="status">


        <span class="visually-hidden">

            Loading...

        </span>


    </div>



    <p>

        Loading data...

    </p>



</div>


</template>



<script setup>

// No script required currently

</script>

<style scoped>


.loading-container{


    min-height:250px;

    display:flex;

    flex-direction:column;

    align-items:center;

    justify-content:center;

    color:#64748B;


}



.spinner-border{


    width:45px;

    height:45px;

    margin-bottom:15px;


}



p{


    font-size:15px;

    font-weight:500;


}


</style>