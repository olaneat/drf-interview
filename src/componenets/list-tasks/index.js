import React, {useState, useEffect} from "react";
import Services from "../../services";
import Style from './style.module.css'
import DeleteIcon from '@mui/icons-material/Delete';
import EditIcon from '@mui/icons-material/Edit';
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";



const TaskList = () =>{
    let [taskLists, setTasks] =  useState([])    
    const navigate = useNavigate() 
    useEffect(()=>{
        fetchTask()
    },[])

    function fetchTask(){
        
        Services.taskList().then((res)=>{
            let tasks = res.data
            setTasks(tasks)
            console.log(taskLists)

        })

        
    }
    function deleteTask(task){
        Services.deleteTask(task.id).then((res)=>{
            console.log(res)
            taskLists.filter((item)=>task.id !== item.id)
            taskLists = taskLists
        })
    }

    const updateTask = (id)=>{
        navigate(`/update-task/${id}`)
    }

    return(
        <div className="container">
            <div className={`${Style.row} row`}>
                <div className={`${Style.lis} col-12`}>
                {taskLists?.map((task)=> {
                        return<div className="row">
                                <p className="col-10"><Link to={`/update/${task.id}`} className={`${Style.link}`}>{task.name}</Link></p>
                                <p className="col-1" onClick={()=>deleteTask(task)}><DeleteIcon/></p>
                                <p className="col-1" onClick={()=>updateTask(task.id)}><EditIcon/></p>
                            </div>
                    })}
                </div>
            </div>
            

        </div>
    )


}


export default TaskList