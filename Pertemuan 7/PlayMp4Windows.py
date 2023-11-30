import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        self.root.configure(bg='#F67828')
        
        # Create a VideoCapture object
        self.cap = cv2.VideoCapture()
        
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Create a label to display the video frames
        self.label = tk.Label(self.frame)
        self.label.pack(padx=10, pady=10)

        # Create buttons
        self.btn_open = tk.Button(self.frame, text="Open Video", command=self.open_video, bg='#2ecc71', fg='white')
        self.btn_open.pack(pady=5)

        self.btn_play = tk.Button(self.frame, text="Play", command=self.play_video, bg='#2ecc71', fg='white')
        self.btn_play.pack(pady=5)
        
        self.btn_stop = tk.Button(self.frame, text="restart", command=self.stop_video, bg='#2ecc71', fg='white')
        self.btn_stop.pack(pady=5)

        self.btn_exit = tk.Button(self.frame, text="Exit", command=root.destroy, bg='#ff0000', fg='white')
        self.btn_exit.pack(pady=5)

    def open_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
        self.cap.open(file_path)

        if file_path:
            self.video_path = file_path
            self.cap = cv2.VideoCapture(self.video_path)


    def play_video(self):
        if self.cap and not self.cap.isOpened():
                self.cap = cv2.VideoCapture(self.video_path)
                
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:   
                # Convert the frame to RGB format
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to ImageTk format
                img = Image.fromarray(rgb_frame)
                img_tk = ImageTk.PhotoImage(img)

                # Update the label with the new frame
                self.label.img_tk = img_tk
                self.label.config(image=img_tk)
                self.root.update()

                # Pause for a short time (approximately 33 milliseconds for 30 fps)
                self.root.after(15, self.play_video)
                
            else:
                # Menghentikan video jika sudah selesai
                self.stop_video()

    def stop_video(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()
            cv2.destroyAllWindows()
            
if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
