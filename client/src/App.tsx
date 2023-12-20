
function App() {
  
  const encender = () => {
    fetch('http://localhost:8000/encender')
      .then((res) => res.json())
      .then((data) => {
        console.log({ data })
      })
  }

  const apagar = () => {
    fetch('http://localhost:8000/apagar')
      .then((res) => res.json())
      .then((data) => {
        console.log({ data })
      })
  }

  return (
    <main className="w-[300px] flex gap-4 p-4">
      <button onClick={encender} className="px-10 py-2 bg-green-600 rounded">ON</button>
      <button  onClick={apagar} className="px-10 py-2 bg-red-600 rounded">OFF</button>
    </main>
  )
}

export default App
