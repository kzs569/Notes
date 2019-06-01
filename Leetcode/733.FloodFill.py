class Solution:
	#recursive dfs
    def floodFill(self,image, sr, sc, newColor):
        import numpy as np
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.width = len(image)
        self.length = len(image[0])
        if (sr<0) or (sr >= self.width):
            return
        if (sc<0) or (sc >= self.length):
            return
        oldColor = image[sr][sc]
        self.image = image
        self.status = np.zeros([self.width,self.length])
        self.dfs(sr,sc,oldColor,newColor)
        return self.image


    def dfs(self,sr,sc,oldColor,newColor):
        
        if (sr<0) or (sr >= self.width):
            return
        if (sc<0) or (sc >= self.length):
            return
        
        pixel = self.image[sr][sc]
        #print("current location : %s %s,color : %s" % (sr,sc,pixel))
        if pixel == oldColor and self.status[sr][sc] == 0:
            self.image[sr][sc] = newColor
            self.status[sr][sc] = 1
            self.dfs(sr+1,sc,oldColor,newColor)
            self.dfs(sr,sc+1,oldColor,newColor)
            self.dfs(sr-1,sc,oldColor,newColor)
            self.dfs(sr,sc-1,oldColor,newColor)

      #iterative bfs
      def floodFill(self,image,sr,sc,newColor):
      	  dxs = [1,0,-1,0]
      	  dys = [0,1,0,-1]
      	  queue = [(sr,sc)]
      	  oldColor = image[sr][sc]
      	  image[sr][sc] = newColor
      	  while queue:
      	  	x,y = queue.pop(0)
      	  	for dx,dy in zip(dxs,dys):
      	  		nx,ny = x + dx,y + dy
      	  		if 0 <= nx <len(image) and 0 <= ny < len(image[0]):
      	  			if image[nx][ny] != newColor and image[nx][ny] == oldColor:
      	  				image[nx][ny] = newColor
      	  				queue.append((nx,ny))
      	  return image;


