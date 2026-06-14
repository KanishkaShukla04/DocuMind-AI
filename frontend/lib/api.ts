export async function uploadFile(files: File[]) {

  const formData = new FormData();

  files.forEach((file)=>{
    formData.append("files", file);
  });


  const response = await fetch(
    "http://127.0.0.1:8000/upload/",
    {
      method:"POST",
      body:formData
    }
  );


  return response.json();
}
export async function askQuestion(
  question: string,
  history: any[]
) {
  const response = await fetch(
    "http://127.0.0.1:8000/chat/",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question,
        history,
      }),
    }
  );

  return response.json();
}