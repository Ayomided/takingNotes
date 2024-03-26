import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import ListItem from '../components/ListItem'

let dummyData = [{"id":"1", "body":"Get milk" }, {"id":"2", "body":"Wash car" }, {"id":"3", "body":"Start coding"}]

const Notes = () => {
    let[notes, setNotes] = useEffect(dummyData)
  return (
    <div>
        <Link to={'/add'}>
            Add
        </Link>
        <ul>
            {notes.map((note) => (
                <li key={note.id}><ListItem note={note}/></li>
            ))}
        </ul>
    </div>
  )
}

export default Notes