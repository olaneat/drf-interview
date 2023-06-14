import React, {useState, useEffect} from "react";
import Style from './task.module.css'
import Services from "../../services";
import {set, useForm} from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';
import { useParams } from 'react-router-dom';
import { useNavigate } from "react-router-dom";

const NewTask = ()=>{

    useEffect(()=>{
        if(!isCreateMode){
            Services.getTaskById(id).then(data=>{
                const task = data.data.data
                const fields =  ['name']
                fields.forEach(field =>setValue(field, task[field]))
                setTaskName(task)
            })
        }
    },[])
    const navigate = useNavigate()
    const params = useParams()
    const validationSchema = Yup.object().shape({
        taskName: Yup.string()
            .required('Title is required'),
        
    })  
    const {  setValue } = useForm({
        resolver: yupResolver(validationSchema)
    });
    const id = params.id
    const isCreateMode = !id
    const [taskName, setTaskName] = useState('')

    const [complete, setcomplete] = useState(Boolean)

   
    const form = {
        taskName: taskName,
    }
   
   function createNewTask(){
        console.log(taskName)    
        Services.createTask(taskName).then((res)=>{navigate('/')})    
    }
    function updateTask(id){
      
         Services.updateTask(id, taskName).then((res)=>{
            console.log(res)
            navigate('/')
        console.log('update')

          

        })
    }    

   function submit(event){
    event.preventDefault()
    return isCreateMode 
        ? createNewTask()
        : updateTask(id)
    navigate([''])
    }
   
    return (
        <div className={`${Style.container} container` }>
            <div className="row">
                <h2>Welcome, What are we doing today </h2>
                <form >
                    <div className={`${Style.fieldDiv} form-group`}>
                    <input
                        value={taskName?.name}
                        onChange={e=>setTaskName({...taskName, name:e.target.value})}
                        placeholder="Enter Task Name"
                        className="form-control"
                    />
                    </div>
                 <button onClick={submit} className={`${Style.btn} btn btn-success`}>Submit Task</button>   
                </form>
            </div>
        </div>
   )

}


export default NewTask