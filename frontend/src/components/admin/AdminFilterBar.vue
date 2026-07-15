<script setup>


defineProps({

    modelValue:{
        type:String,
        default:""
    },


    options:{
        type:Array,
        default:()=>[]
    }

})


defineEmits([

    "update:modelValue"

])


</script>


<template>


<select

    class="form-select"

    :value="modelValue"

    @change="
    $emit(
        'update:modelValue',
        $event.target.value
    )
    "

>


<option value="">

    All Status

</option>



<option

    v-for="item in options"

    :key="item"

>

    {{item}}

</option>


</select>


</template>



<style scoped>


.form-select{

    height:42px;

    border-radius:8px;

    border:1px solid #e2e8f0;

    font-size:14px;

}


</style>