using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Abstraction
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            List<Video> videos = new();
            Video video1 = new("Title 1", "Author 1", 312f);
            video1.AddComment(new Comment("Commentor 1", "Comment 1"));
            video1.AddComment(new Comment("Commentor 2", "Comment 2"));
            video1.AddComment(new Comment("Commentor 3", "Comment 3"));
            videos.Add(video1);

            Video video2 = new("Title 2", "Author 2", 452f);
            video2.AddComment(new Comment("Commentor 4", "Comment 4"));
            video2.AddComment(new Comment("Commentor 5", "Comment 5"));
            video2.AddComment(new Comment("Commentor 6", "Comment 6"));
            videos.Add(video2);

            Video video3 = new("Title 3", "Author 3", 784f);
            video3.AddComment(new Comment("Commentor 7", "Comment 7"));
            video3.AddComment(new Comment("Commentor 8", "Comment 8"));
            video3.AddComment(new Comment("Commentor 9", "Comment 9"));
            videos.Add(video3);

            foreach (Video video in videos)
            {
                video.DisplayVideo();
            }
        }
    }
}