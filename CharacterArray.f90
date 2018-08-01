! '''
!     Neuromuscular simulator in Python.
!     Copyright (C) 2018  Renato Naville Watanabe

!     This program is free software: you can redistribute it and/or modify
!     it under the terms of the GNU General Public License as published by
!     the Free Software Foundation, either version 3 of the License, or
!     any later version.

!     This program is distributed in the hope that it will be useful,
!     but WITHOUT ANY WARRANTY; without even the implied warranty of
!     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
!     GNU General Public License for more details.

!     You should have received a copy of the GNU General Public License
!     along with this program.  If not, see <http://www.gnu.org/licenses/>.

!     Contact: renato.watanabe@ufabc.edu.br
! '''

module StringClass
    implicit none
    private
    public :: String

    type String
        character(len = 80) :: string

       contains     
    end type String

    interface String
        module procedure init_String
    end interface String
    
    contains

        type (String) function init_String(newString)
            character(len = 80), intent(in) :: newString 

            init_String%string = trim(newString)
        end function

end module StringClass

module CharacterArrayClass
    use StringClass
    implicit none
    private
    public :: CharacterArray

    type CharacterArray
        type(String), dimension(:), allocatable :: item

       contains   
            procedure :: AddToList   
    end type CharacterArray

    interface CharacterArray
        module procedure init_CharacterArray
    end interface CharacterArray
    
    contains

        type (CharacterArray) function init_CharacterArray()
            if (allocated(init_CharacterArray%item)) then
                 deallocate(init_CharacterArray%item)
            end if
        end function

        subroutine AddToList(self, newString)
            class(CharacterArray), intent(inout) :: self
            character(len = 80), intent(in) :: newString
            type(CharacterArray) :: clist
            integer :: isize, i

            clist = CharacterArray()
            
            
            if(allocated(self%item)) then
                isize = size(self%item)
                allocate(clist%item(isize+1))
                do i=1,isize          
                    clist%item(i) = self%item(i)
                end do
                clist%item(isize+1) = String(newString)

                deallocate(self%item)
                allocate(self%item(isize+1))
                
                do i=1, isize + 1         
                    self%item(i) = clist%item(i)
                end do

            else
                allocate(self%item(1))
                self%item(1) = String(newString)
            end if


        end subroutine
end module CharacterArrayClass


