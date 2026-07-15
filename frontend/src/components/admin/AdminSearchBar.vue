<script setup>

defineProps({

    modelValue:{
        type:String,
        default:""
    },

    placeholder:{
        type:String,
        default:"Search..."
    }

})


defineEmits([

    "update:modelValue"

])


</script>


<template>


<div class="search-wrapper">


    <i class="bi bi-search"></i>


    <input

        :value="modelValue"

        @input="
        $emit(
            'update:modelValue',
            $event.target.value
        )
        "

        :placeholder="placeholder"

    />


</div>


</template>



<style scoped>


.search-wrapper{

    display:flex;

    align-items:center;

    gap:10px;

    height:42px;

    border:1px solid #e2e8f0;

    border-radius:8px;

    background:white;

    padding:0 15px;

}


.search-wrapper i{

    color:#64748b;

}


.search-wrapper input{

    border:none;

    outline:none;

    width:100%;

    font-size:14px;

}


</style>