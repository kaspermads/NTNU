import React, { useState, useEffect } from "react";

const App: React.FC = () => {
  const [patients, setPatients] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    fetch("https://www.kaspergaupmadsen.no/Patients/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setPatients(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <h1>Patients List</h1>
      <ul>
        {patients.map((patient, index) => (
          <li key={index}>
            {patient.first_name} {patient.last_name} - Birthdate:{" "}
            {patient.birthDate}
          </li>
        ))}
      </ul>
    </>
  );
};

export default App;
