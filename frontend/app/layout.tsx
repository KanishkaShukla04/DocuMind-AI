import "./global.css";

export const metadata = {
  title: "DocuMind AI",
  description: "AI Document Intelligence",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}