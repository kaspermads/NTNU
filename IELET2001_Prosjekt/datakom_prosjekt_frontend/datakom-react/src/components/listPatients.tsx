function ListPatients() {
  let patients = ["John Doe", "Jane Doe", "John Smith", "Jane Smith"];
  patients = [];

  const;

  return (
    <>
      <h1>List of Patients</h1>
      {patients.length === 0 ? <p>No patients found</p> : null}
      <ul className="list-group">
        {patients.map((patients) => (
          <li key={patients}>{patients}</li>
        ))}
      </ul>
    </>
  );
}
export default ListPatients;
